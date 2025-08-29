import threading, os
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox
    _HAVE_DND = True
except Exception:
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox
    _HAVE_DND = False

from . import core
from .format_spec import StegFormatError

class DragDropEntry(ttk.Frame):
    def __init__(self, master, label_text, directory=False, **kwargs):
        super().__init__(master, **kwargs)
        self.directory = directory
        self.var = tk.StringVar()
        ttk.Label(self, text=label_text).pack(anchor='w')
        self.entry = ttk.Entry(self, textvariable=self.var, width=60)
        self.entry.pack(side='left', fill='x', expand=True)
        browse_cmd = self.browse_dir if directory else self.browse_file
        ttk.Button(self, text='Browse', command=browse_cmd).pack(side='left')
        if _HAVE_DND:
            try:
                self.entry.drop_target_register(DND_FILES)
                self.entry.dnd_bind('<<Drop>>', self._on_drop)
            except Exception:
                pass

    def _on_drop(self, event):
        data = event.data
        if data.startswith('{') and data.endswith('}'):
            # On Windows spaces in path come wrapped in {}
            data = data[1:-1]
        # Support multiple; take first
        first = data.split() [0]
        if self.directory and not os.path.isdir(first):
            # If a file dropped where dir expected, use its parent
            first = os.path.dirname(first)
        self.var.set(first)

    def browse_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.var.set(path)

    def browse_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.var.set(path)

    def get(self):
        return self.var.get().strip()

class App((TkinterDnD.Tk if _HAVE_DND else tk.Tk)):
    def __init__(self):
        super().__init__()
        self.title('Steg Tool')
        self.geometry('760x480')
        nb = ttk.Notebook(self)
        nb.pack(fill='both', expand=True)
        self.pack_tab = ttk.Frame(nb)
        self.unpack_tab = ttk.Frame(nb)
        nb.add(self.pack_tab, text='Encrypt / Hide')
        nb.add(self.unpack_tab, text='Decrypt / Extract')
        self.build_pack()
        self.build_unpack()
        if not _HAVE_DND:
            ttk.Label(self, text='(Optional drag & drop: install tkinterdnd2)', foreground='gray').pack(anchor='e', padx=4, pady=2)

    def build_pack(self):
        f = self.pack_tab
        self.carrier = DragDropEntry(f, 'Carrier File:')
        self.carrier.pack(fill='x', padx=10, pady=5)
        self.payload = DragDropEntry(f, 'Payload File to Hide:')
        self.payload.pack(fill='x', padx=10, pady=5)
        out_frame = ttk.Frame(f); out_frame.pack(fill='x', padx=10, pady=5)
        ttk.Label(out_frame, text='Output (optional):').pack(anchor='w')
        self.out_var = tk.StringVar()
        ttk.Entry(out_frame, textvariable=self.out_var, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(out_frame, text='Browse', command=self.choose_out).pack(side='left')
        pass_frame = ttk.Frame(f); pass_frame.pack(fill='x', padx=10, pady=5)
        ttk.Label(pass_frame, text='Password (optional):').pack(anchor='w')
        self.pass_var = tk.StringVar()
        ttk.Entry(pass_frame, textvariable=self.pass_var, show='*', width=40).pack(anchor='w')
        self.pack_btn = ttk.Button(f, text='Hide File', command=self.do_pack)
        self.pack_btn.pack(pady=15)
        self.pack_status = tk.StringVar()
        ttk.Label(f, textvariable=self.pack_status, foreground='blue').pack()

    def build_unpack(self):
        f = self.unpack_tab
        self.steg = DragDropEntry(f, 'Steg File:')
        self.steg.pack(fill='x', padx=10, pady=5)
        self.dest_dir = DragDropEntry(f, 'Destination Directory:', directory=True)
        self.dest_dir.pack(fill='x', padx=10, pady=5)
        if not _HAVE_DND:
            ttk.Button(self.dest_dir, text='Browse Dir', command=self.choose_dir).pack(side='left')
        pass_frame = ttk.Frame(f); pass_frame.pack(fill='x', padx=10, pady=5)
        ttk.Label(pass_frame, text='Password (if used):').pack(anchor='w')
        self.upass_var = tk.StringVar()
        ttk.Entry(pass_frame, textvariable=self.upass_var, show='*', width=40).pack(anchor='w')
        self.unpack_btn = ttk.Button(f, text='Extract Hidden File', command=self.do_unpack)
        self.unpack_btn.pack(pady=15)
        self.unpack_status = tk.StringVar()
        ttk.Label(f, textvariable=self.unpack_status, foreground='green').pack()

    def choose_out(self):
        path = filedialog.asksaveasfilename()
        if path:
            self.out_var.set(path)

    def choose_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.dest_dir.var.set(path)

    def do_pack(self):
        carrier = self.carrier.get(); payload = self.payload.get()
        if not (os.path.isfile(carrier) and os.path.isfile(payload)):
            messagebox.showerror('Error', 'Carrier or payload path invalid')
            return
        out = self.out_var.get().strip() or None
        pwd = self.pass_var.get().strip() or None
        self.pack_btn.config(state='disabled'); self.pack_status.set('Processing...')
        def worker():
            try:
                out_path = core.pack(carrier, payload, out, pwd)
                self.pack_status.set(f'Success -> {out_path}')
            except Exception as e:
                self.pack_status.set('Failed')
                messagebox.showerror('Pack Error', str(e))
            finally:
                self.pack_btn.config(state='normal')
        threading.Thread(target=worker, daemon=True).start()

    def do_unpack(self):
        steg = self.steg.get(); dest = self.dest_dir.get()
        if not os.path.isfile(steg):
            messagebox.showerror('Error', 'Steg file invalid')
            return
        if not dest:
            messagebox.showerror('Error', 'Destination directory required')
            return
        pwd = self.upass_var.get().strip() or None
        self.unpack_btn.config(state='disabled'); self.unpack_status.set('Processing...')
        def worker():
            try:
                out_path = core.find_and_unpack(steg, dest, pwd)
                self.unpack_status.set(f'Extracted -> {out_path}')
            except StegFormatError as e:
                self.unpack_status.set('Not found / Invalid')
                messagebox.showwarning('Format', str(e))
            except Exception as e:
                self.unpack_status.set('Failed')
                messagebox.showerror('Unpack Error', str(e))
            finally:
                self.unpack_btn.config(state='normal')
        threading.Thread(target=worker, daemon=True).start()


def main():
    App().mainloop()

if __name__ == '__main__':
    main()
