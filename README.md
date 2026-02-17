# NigudhaX - Advanced Steganography Tool

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

## 📖 The Story Behind the Name

### Etymology: निगूढ (Nigudha)

**NigudhaX** derives its name from the Sanskrit word **"निगूढ" (Nigudha)**, which means "hidden," "concealed," or "secret." In ancient Sanskrit literature, this word was used to describe things that are deliberately kept hidden from plain sight, mysteries that require special knowledge to uncover.

### Why "NigudhaX"?

The **"X"** in NigudhaX represents the **unknown** - the hidden content, the secret payload, the concealed information that lies beneath the surface of an ordinary file. Just as "X" marks the spot in treasure maps, **NigudhaX** marks the intersection of ancient wisdom about secrecy and modern digital steganography.

**Nigudha (निगूढ)** + **X (the unknown)** = **NigudhaX**: *A tool to hide the unknown*

This name perfectly captures the essence of steganography - the art and science of concealing information within other non-secret data. While the world sees an innocent image, audio, or video file, those with the right knowledge can uncover the hidden treasure within.

---

## 🎯 What is Steganography?

Steganography is the practice of concealing messages or information within other non-secret data. Unlike cryptography, which makes data unreadable, steganography makes data invisible. The word itself comes from Greek: *steganos* (covered) and *graphein* (writing) - literally "covered writing."

**Real-world examples:**
- Hiding secret messages in photographs
- Embedding data in audio files
- Concealing documents within video files
- Watermarking digital media

---

## 🚀 Project Overview

**NigudhaX** is a cross-platform Python-based steganography tool with a user-friendly graphical interface. It allows you to hide any file (payload) inside another file (carrier) such as images, audio, or video files. The hidden data is completely invisible to casual inspection and can only be extracted using NigudhaX itself.

### Key Highlights

- **🎨 User-Friendly GUI**: Easy-to-use interface with drag & drop support
- **🔒 Optional Encryption**: Password-protect your hidden files with ChaCha20 encryption
- **✅ Integrity Verification**: SHA-256 checksums ensure data integrity
- **📁 Universal Format**: Hide ANY file type inside ANY carrier file
- **🎭 Stealth**: Carrier files remain fully functional after embedding
- **🔄 Cross-Platform**: Works on Windows, macOS, and Linux

---

## ✨ Features & Advantages

### 1. **Complete Invisibility**
   - The carrier file (image/audio/video) remains fully viewable and functional
   - No visual or audible degradation
   - Hidden data is appended in a way that doesn't affect the carrier's display

### 2. **Strong Security**
   - Custom magic header prevents accidental extraction by other tools
   - Optional password protection with ChaCha20 encryption (via PyNaCl)
   - PBKDF2 key derivation with 200,000 iterations
   - SHA-256 integrity verification

### 3. **Flexibility**
   - Hide documents in photos (.jpg, .png)
   - Conceal files in audio tracks (.mp3, .wav)
   - Embed data in videos (.mp4, .avi)
   - Any file type can be a carrier or payload

### 4. **Easy to Use**
   - Simple two-step process: Hide and Extract
   - Drag and drop file selection
   - No technical knowledge required
   - Clear status messages and error handling

### 5. **Practical Applications**
   - **Privacy**: Share sensitive documents discreetly
   - **Security**: Add an extra layer of protection to confidential files
   - **Digital Watermarking**: Embed ownership information in media files
   - **Secure Communication**: Exchange information without drawing attention
   - **Academic Research**: Study steganography and information hiding techniques

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- tkinter (usually bundled with Python)

### Step 1: Clone the Repository
```bash
git clone https://github.com/thetirthchauhan/NigudhaX.git
cd NigudhaX
```

### Step 2: Install Dependencies
```bash
pip install -r steg_tool/requirements.txt
```

**Dependencies:**
- `pynacl>=1.5.0` - For ChaCha20 encryption (optional, falls back to XOR if unavailable)
- `tkinterdnd2` - For drag & drop support (optional)

---

## 📚 User Manual

### Method 1: Running from Source

#### Hiding a File (Encryption)

1. **Launch the application:**
   ```bash
   python -m steg_tool.app
   ```

2. **Select the "Encrypt / Hide" tab**

3. **Choose your files:**
   - **Carrier File**: Select an image, audio, or video file that will carry the hidden data
     - Example: `vacation_photo.jpg`, `song.mp3`, `video.mp4`
   - **Payload File to Hide**: Select any file you want to hide
     - Example: `secret_document.pdf`, `passwords.txt`, `confidential.docx`

4. **Set output location (optional):**
   - Leave blank to create `<carrier_name>_packed.<ext>` in the same folder
   - Or specify a custom output path

5. **Set password (optional but recommended):**
   - Enter a strong password to encrypt the hidden file
   - Without a password, the file is only hidden, not encrypted

6. **Click "Hide File"**
   - Wait for the "Success" message
   - The output file will look and behave exactly like the original carrier

#### Extracting a Hidden File (Decryption)

1. **Launch the application:**
   ```bash
   python -m steg_tool.app
   ```

2. **Select the "Decrypt / Extract" tab**

3. **Choose the steg file:**
   - Select the file containing hidden data (e.g., `vacation_photo_packed.jpg`)

4. **Choose destination directory:**
   - Select where to save the extracted file

5. **Enter password (if used during hiding):**
   - Must match the password used during encryption

6. **Click "Extract Hidden File"**
   - The original hidden file will be restored with its original name
   - Success message will show the output path

### Method 2: Using Standalone Executable (Optional)

If you build the standalone executable using PyInstaller:

```bash
pyinstaller -F -w steg_tool/app.py -n StegTool
```

Then simply run:
```bash
dist/StegTool.exe  # On Windows
dist/StegTool      # On Linux/Mac
```

The GUI works the same way as described above.

---

## 💡 Usage Examples

### Example 1: Hide a Document in a Photo

**Scenario**: You want to share a confidential PDF with a colleague securely.

1. Start NigudhaX
2. Carrier: `beach_vacation.jpg` (any photo from your collection)
3. Payload: `quarterly_report.pdf` (your confidential document)
4. Password: `SecurePass2024!`
5. Output: `beach_vacation_packed.jpg`
6. Share `beach_vacation_packed.jpg` via email or cloud storage
7. Recipient uses NigudhaX to extract with the password

**Result**: The image looks normal to anyone viewing it, but contains your hidden PDF!

### Example 2: Embed Source Code in Music

**Scenario**: Back up your source code in an audio file.

1. Start NigudhaX
2. Carrier: `favorite_song.mp3`
3. Payload: `project_backup.zip` (compressed source code)
4. Password: (optional)
5. Output: `favorite_song_packed.mp3`

**Result**: The music plays normally, but contains your entire project backup!

### Example 3: Hide Multiple Files

**Scenario**: Hide several files at once.

1. First, compress your files: Create `secrets.zip` containing all files
2. Start NigudhaX
3. Carrier: `wallpaper.png`
4. Payload: `secrets.zip`
5. Password: Your strong password
6. Output: `wallpaper_packed.png`

**Result**: All your files hidden in one image!

---

## 🔧 Technical Details

### Custom Container Format

NigudhaX uses a proprietary format to ensure hidden data can only be extracted with this tool:

```
┌─────────────────────────────────────┐
│ Original Carrier File (unchanged)   │
├─────────────────────────────────────┤
│ MAGIC HEADER: 'STEGTOOL' (8 bytes) │
│ VERSION: 0x01 (1 byte)              │
│ FLAGS: Encryption bit (1 byte)      │
│ ORIGINAL_CARRIER_SIZE (8 bytes)     │
│ PAYLOAD_NAME_LENGTH (2 bytes)       │
│ PAYLOAD_NAME (variable, UTF-8)      │
│ PAYLOAD_SIZE (8 bytes)              │
│ SHA-256 CHECKSUM (32 bytes)         │
│ [If encrypted]                      │
│   NONCE_LENGTH (1 byte)             │
│   NONCE (variable)                  │
│ ENCRYPTED/RAW PAYLOAD DATA          │
└─────────────────────────────────────┘
```

### Encryption Details

- **With PyNaCl**: ChaCha20-Poly1305 authenticated encryption
- **Fallback**: Simple XOR with derived key (if PyNaCl unavailable)
- **Key Derivation**: PBKDF2-HMAC-SHA256 with 200,000 iterations
- **Integrity**: SHA-256 checksum verification on extraction

### Why This Approach?

- **Carrier Compatibility**: Since data is appended (not embedded in pixels/bits), the carrier file remains fully viewable
- **No Quality Loss**: Original carrier quality is preserved 100%
- **Detection Resistance**: Casual inspection won't reveal hidden data
- **Format Flexibility**: Works with any binary file format

---

## ⚠️ Security Considerations

### What NigudhaX Does Well:
✅ Hides data from casual inspection  
✅ Protects data with strong encryption (when password is used)  
✅ Ensures data integrity with checksums  
✅ Makes steg files look like normal files

### Limitations:
❌ **Not Pixel-Level Steganography**: Data is appended, not embedded in image pixels or audio samples  
❌ **File Size Analysis**: The steg file will be larger than the original carrier  
❌ **Professional Detection**: Steganalysis tools can detect appended data  

### Best Practices:
1. **Always use a strong password** for sensitive data
2. **Use common carrier files** (photos, music) that won't raise suspicion
3. **Don't use tiny carriers** with large payloads (size increase is noticeable)
4. **This is not for high-security environments** - use proper encryption tools for classified data
5. **For casual privacy and learning purposes** - perfect for academic projects and personal use

---

## 📁 Project Structure

```
NigudhaX/
├── steg_tool/              # Main package
│   ├── __init__.py         # Package initialization
│   ├── __main__.py         # Entry point
│   ├── app.py              # GUI application
│   ├── core.py             # Core steganography logic
│   ├── format_spec.py      # Format specifications
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Technical README
├── LICENSE                 # MIT License
├── StegTool.spec           # PyInstaller specification
├── keep.txt                # Quick reference
└── README.md               # This file
```

---

## 🎓 Educational Value

NigudhaX is an excellent tool for learning about:

1. **Steganography Fundamentals**: Understanding how information hiding works
2. **Cryptography Basics**: Encryption, key derivation, and integrity checks
3. **File Format Analysis**: Binary file structures and data appending techniques
4. **Python Programming**: GUI development with tkinter, file I/O, and threading
5. **Software Security**: Thinking about threat models and security limitations

Perfect for:
- Computer Science students studying cybersecurity
- Information security courses and projects
- Digital forensics education
- Privacy and cryptography research

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Tirth

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 👨‍💻 Author

**Tirth Chauhan**  
- GitHub: [@thetirthchauhan](https://github.com/thetirthchauhan)
- Project: [NigudhaX](https://github.com/thetirthchauhan/NigudhaX)

---

## 🙏 Acknowledgments

- Inspired by the ancient art of secret communication
- Built with Python and the amazing open-source community
- Special thanks to the creators of PyNaCl for modern cryptography

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the [User Manual](#-user-manual) section
2. Review the [Technical Details](#-technical-details)
3. Open an issue on GitHub

---

**Remember**: NigudhaX is designed for educational purposes and casual privacy needs. For high-security requirements, consult with security professionals and use industry-standard tools.

*"The best place to hide a secret is in plain sight."* 🎭
