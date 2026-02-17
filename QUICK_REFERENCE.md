# NigudhaX - Quick Reference

## 🎯 What is NigudhaX?

A steganography tool to hide files inside images, audio, or video files.

**Name Origin:** Nigudha (निगूढ) = Sanskrit word for "hidden" + X = "the unknown"

---

## ⚡ Quick Start

### Install & Run
```bash
# Clone repository
git clone https://github.com/thetirthchauhan/NigudhaX.git
cd NigudhaX

# Install dependencies
pip install -r steg_tool/requirements.txt

# Run application
python -m steg_tool.app
```

---

## 📋 Basic Operations

### Hide a File
1. Open "Encrypt / Hide" tab
2. Select carrier file (image/audio/video)
3. Select payload file (file to hide)
4. Enter password (optional but recommended)
5. Click "Hide File"

### Extract a File
1. Open "Decrypt / Extract" tab
2. Select steg file (file with hidden data)
3. Select destination folder
4. Enter password (if used during hiding)
5. Click "Extract Hidden File"

---

## 🎓 For University Submission

### What's Included:
- ✅ **README.md** - Full project documentation with name story
- ✅ **USER_GUIDE.md** - Detailed step-by-step manual
- ✅ **EMAIL_TEMPLATE.md** - Professional email for professor
- ✅ **Source Code** - Well-commented Python code
- ✅ **Technical Docs** - Format specifications and details

### Key Points for Your Report:
1. **Name Significance**: Sanskrit origin + modern cryptography
2. **Technology**: Python, Tkinter GUI, ChaCha20 encryption
3. **Features**: Hide any file, optional encryption, integrity checks
4. **Use Cases**: Privacy, security, digital watermarking, education
5. **Advantages**: User-friendly, cross-platform, secure

---

## 📧 Email Your Professor

Use the template in `EMAIL_TEMPLATE.md`. Just replace:
- [Professor's Name]
- [Course Name/Code]
- [Your Full Name]
- [Your Student ID]

---

## 🔑 Key Features to Highlight

1. **Meaningful Name** - Sanskrit etymology shows cultural depth
2. **Real Steganography** - Not just encryption, actual hiding
3. **User-Friendly** - GUI with drag-and-drop
4. **Secure** - Optional ChaCha20 encryption + SHA-256 integrity
5. **Practical** - Works with any file types
6. **Well-Documented** - Complete manuals and guides

---

## 💡 Project Advantages

### Technical:
- Cross-platform (Windows/Mac/Linux)
- Modern encryption (ChaCha20-Poly1305)
- Custom file format
- Integrity verification
- Fallback mechanisms

### User Experience:
- Simple GUI
- Clear instructions
- Drag & drop support
- Status messages
- Error handling

### Educational:
- Demonstrates steganography concepts
- Shows cryptography application
- Python best practices
- GUI development
- Binary file handling

---

## 📚 Documentation Structure

```
NigudhaX/
├── README.md              ← Main documentation (READ FIRST)
├── USER_GUIDE.md          ← Step-by-step manual
├── EMAIL_TEMPLATE.md      ← Email for professor
├── QUICK_REFERENCE.md     ← This file
├── steg_tool/
│   ├── README.md          ← Technical details
│   ├── app.py             ← GUI application
│   ├── core.py            ← Core logic
│   ├── format_spec.py     ← Format specifications
│   └── requirements.txt   ← Dependencies
└── LICENSE                ← MIT License
```

---

## 🎨 Example Use Cases

### 1. Student Use Case
**Scenario:** Submit project securely
- Hide: `project_report.pdf` in `cover_image.jpg`
- Share: `cover_image_packed.jpg` with password
- Professor extracts with NigudhaX + password

### 2. Privacy Use Case
**Scenario:** Backup sensitive documents
- Hide: `personal_docs.zip` in `music_track.mp3`
- Store: Music file in cloud (no one suspects)
- Restore: Extract when needed with password

### 3. Learning Use Case
**Scenario:** Understand steganography
- Experiment with different file types
- Study the code and format
- Learn about encryption and hiding

---

## 🔍 What Makes This Project Special?

1. **Cultural Connection**: Sanskrit name with meaning
2. **Complete Implementation**: Not just a proof-of-concept
3. **Professional Quality**: Error handling, validation, docs
4. **Security-Focused**: Encryption, integrity, best practices
5. **User-Centric**: GUI, documentation, examples
6. **Educational Value**: Great for learning and teaching

---

## ⚠️ Important Notes

- **File Size**: Steg file = Carrier + Payload + small overhead
- **Password**: Remember it! No recovery without password
- **Backup**: Keep original files separately
- **Limitations**: This is appending-based, not pixel-level steganography
- **Use Cases**: Educational, casual privacy (not high-security military/gov)

---

## 🎯 For Presentations/Demos

### Show These Steps:
1. Launch application (show GUI)
2. Hide a sample PDF in an image
3. Open the steg image (proves it still works)
4. Extract the PDF successfully
5. Show file size comparison
6. Explain encryption option
7. Show documentation quality

### Talking Points:
- "Nigudha means hidden in Sanskrit..."
- "Notice the image still opens normally..."
- "With password, data is encrypted..."
- "SHA-256 ensures integrity..."
- "Works on any platform..."

---

## 📞 Need Help?

1. **Read**: README.md for overview
2. **Follow**: USER_GUIDE.md for detailed steps
3. **Check**: steg_tool/README.md for technical details
4. **Test**: Try with sample files first
5. **Report**: GitHub issues for bugs

---

## ✅ Pre-Submission Checklist

- [ ] Read all documentation
- [ ] Test the application yourself
- [ ] Prepare sample files for demo
- [ ] Fill in email template
- [ ] Verify GitHub repository is accessible
- [ ] Take screenshots (optional)
- [ ] Write project report (if required)
- [ ] Practice your presentation (if required)

---

**Repository:** https://github.com/thetirthchauhan/NigudhaX

**License:** MIT

**Author:** Tirth Chauhan

---

*Good luck with your submission! 🎓*
