# NigudhaX User Guide

## Complete Step-by-Step Manual

---

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Hiding Files (Encryption)](#hiding-files-encryption)
5. [Extracting Files (Decryption)](#extracting-files-decryption)
6. [Advanced Usage](#advanced-usage)
7. [Troubleshooting](#troubleshooting)
8. [Tips & Best Practices](#tips--best-practices)

---

## Introduction

Welcome to NigudhaX! This user guide will walk you through everything you need to know to use this steganography tool effectively.

### What Will You Learn?
- How to hide any file inside images, audio, or video files
- How to protect hidden files with passwords
- How to extract hidden files
- Best practices for secure file concealment

### Time Required
- Installation: 5 minutes
- Learning basic operations: 10 minutes
- Becoming proficient: 30 minutes

---

## Installation

### For Windows Users

1. **Check Python Installation**
   - Open Command Prompt (press Win+R, type `cmd`, press Enter)
   - Type: `python --version`
   - You should see Python 3.8 or higher
   - If not installed, download from [python.org](https://www.python.org/downloads/)

2. **Download NigudhaX**
   - Download the ZIP file from GitHub
   - Extract to a folder (e.g., `C:\NigudhaX`)

3. **Install Dependencies**
   - Open Command Prompt in the NigudhaX folder
   - Type: `pip install -r steg_tool/requirements.txt`
   - Press Enter and wait for installation to complete

4. **Verify Installation**
   - Type: `python -m steg_tool.app`
   - The NigudhaX window should open

### For macOS/Linux Users

1. **Check Python Installation**
   ```bash
   python3 --version
   ```
   Should show Python 3.8 or higher

2. **Download and Setup**
   ```bash
   git clone https://github.com/thetirthchauhan/NigudhaX.git
   cd NigudhaX
   pip3 install -r steg_tool/requirements.txt
   ```

3. **Run**
   ```bash
   python3 -m steg_tool.app
   ```

---

## Getting Started

### Understanding the Interface

When you launch NigudhaX, you'll see a window with two tabs:

1. **Encrypt / Hide Tab** (Left side)
   - Used to hide files inside carrier files
   - Main operation: Concealing data

2. **Decrypt / Extract Tab** (Right side)
   - Used to extract hidden files
   - Main operation: Revealing concealed data

### Key Terms

- **Carrier File**: The "innocent" file that will carry hidden data (e.g., a photo, song, or video)
- **Payload File**: The file you want to hide (e.g., document, archive, source code)
- **Steg File**: The result after hiding - looks like the carrier but contains hidden data
- **Password**: Optional encryption key to protect your hidden data

---

## Hiding Files (Encryption)

### Basic Steps

#### Step 1: Launch NigudhaX
```bash
python -m steg_tool.app
```

#### Step 2: Select the "Encrypt / Hide" Tab
Click on the "Encrypt / Hide" tab if not already selected.

#### Step 3: Choose Carrier File

**Method A: Using Browse Button**
1. Click the "Browse" button next to "Carrier File:"
2. Navigate to your file (e.g., a photo: `vacation.jpg`)
3. Select it and click "Open"

**Method B: Using Drag & Drop** (if available)
1. Open your file explorer
2. Drag the carrier file (e.g., `vacation.jpg`)
3. Drop it in the "Carrier File:" text box

**Good Carrier File Examples:**
- Photos: `family_photo.jpg`, `landscape.png`
- Music: `favorite_song.mp3`, `podcast.wav`
- Videos: `video_clip.mp4`, `tutorial.avi`

#### Step 4: Choose Payload File

**What to Hide (Payload Examples):**
- Documents: `report.pdf`, `notes.docx`, `spreadsheet.xlsx`
- Archives: `project.zip`, `backup.tar.gz`
- Code: `source_code.py`, `website.html`
- Sensitive data: `passwords.txt`, `keys.pem`

**Important:** You can hide ANY file type!

Select your payload file using Browse or Drag & Drop (same as carrier).

#### Step 5: Set Output Location (Optional)

**Option 1: Leave Blank (Recommended for Beginners)**
- NigudhaX will create: `carrier_name_packed.ext`
- Example: If carrier is `photo.jpg`, output will be `photo_packed.jpg`
- Saved in the same folder as the carrier

**Option 2: Specify Custom Path**
- Click "Browse" next to "Output (optional):"
- Choose a location and filename
- **Pro Tip:** Keep the same extension as the carrier for compatibility

#### Step 6: Set Password (Recommended)

**Why Use a Password?**
- Encrypts your hidden data
- Only those with the password can extract
- Adds strong security layer

**Password Guidelines:**
- **Minimum Length:** 8 characters
- **Good Password:** `MySecret2024!Pass`
- **Better Password:** `C0mpl3x&S3cur3!Pwd#2024`
- **Avoid:** Simple words like "password" or "123456"

Type your password in the "Password (optional):" field.

**⚠️ Important:** Remember this password! You'll need it to extract the file.

#### Step 7: Hide the File

1. Click the "Hide File" button
2. Status will show "Processing..."
3. Wait for the success message: `Success -> /path/to/output_file`
4. Done! Your steg file is ready

### What Just Happened?

- Your payload file was embedded into the carrier
- If password was provided, payload was encrypted
- A checksum was calculated for integrity
- The carrier still works normally (image viewable, audio playable, etc.)

---

## Extracting Files (Decryption)

### Basic Steps

#### Step 1: Select the "Decrypt / Extract" Tab
Click on the "Decrypt / Extract" tab.

#### Step 2: Choose Steg File

Select the file containing hidden data:
- This is the file created by the "Hide" operation
- Example: `photo_packed.jpg`, `song_packed.mp3`

Use Browse or Drag & Drop (same as before).

#### Step 3: Choose Destination Directory

**Where to Save the Extracted File:**
1. Click "Browse" (or "Browse Dir" button)
2. Select a folder where you want the extracted file saved
3. The original filename will be preserved

**Example:**
- If you hid `report.pdf`, it will be extracted as `report.pdf`
- You just choose which folder it goes into

#### Step 4: Enter Password (if used)

**Did you use a password when hiding?**
- **YES:** Enter the exact same password
- **NO:** Leave the password field blank

**⚠️ Critical:** Password must match exactly (case-sensitive!)

#### Step 5: Extract the File

1. Click "Extract Hidden File"
2. Status shows "Processing..."
3. Wait for success: `Extracted -> /path/to/extracted_file`
4. Done! Your hidden file is now restored

### Verification

After extraction:
1. Navigate to the destination folder
2. You should see your original file with its original name
3. Open it to verify it's intact

---

## Advanced Usage

### Hiding Multiple Files

**Scenario:** You want to hide several files at once.

**Solution:** Create a ZIP archive first.

1. **Create Archive:**
   - Windows: Select files → Right-click → "Send to" → "Compressed folder"
   - macOS: Select files → Right-click → "Compress items"
   - Linux: `zip -r archive.zip file1 file2 file3`

2. **Hide the Archive:**
   - Carrier: Choose any image/audio/video
   - Payload: Select your `archive.zip`
   - Password: Set a strong password
   - Hide!

3. **Extract:**
   - Extract the ZIP from the steg file
   - Unzip to get all your original files

### Chaining Operations

**Scenario:** Hide File A inside File B, then hide the result inside File C.

**Steps:**
1. Hide `secretA.pdf` in `photo1.jpg` → creates `photo1_packed.jpg`
2. Hide `photo1_packed.jpg` in `photo2.jpg` → creates `photo2_packed.jpg`
3. Result: `photo2_packed.jpg` contains `photo1_packed.jpg` which contains `secretA.pdf`

**Extraction:** Reverse the process (extract twice)

**Use Case:** Double layer of security, though increases file size significantly.

### Using Different File Types

| Carrier Type | Best For | Considerations |
|--------------|----------|----------------|
| **JPEG Images** | Small to medium files | Most common, less suspicious |
| **PNG Images** | Small files | Larger than JPEG, high quality |
| **MP3 Audio** | Medium files | Great for hiding documents |
| **MP4 Video** | Large files | Can hide very large payloads |
| **PDF Documents** | Small files | Unusual but works |
| **ZIP Archives** | Any size | Can itself contain multiple files |

---

## Troubleshooting

### Problem: "Carrier or payload path invalid"

**Cause:** File path is incorrect or file doesn't exist.

**Solution:**
1. Check that both files exist
2. Verify file paths don't contain special characters
3. Try using Browse button instead of typing path

### Problem: "Password required" (during extraction)

**Cause:** File was hidden with a password but you didn't enter one.

**Solution:**
1. Enter the password used during hiding
2. Make sure it's typed correctly (case-sensitive)

### Problem: "Integrity check failed"

**Cause:** File is corrupted or wrong password used.

**Solution:**
1. If password-protected: Verify you're using the correct password
2. If not password-protected: File may be corrupted
3. Try using the original steg file (not a copy that may have been modified)

### Problem: "No hidden data found"

**Cause:** The file doesn't contain NigudhaX hidden data.

**Solution:**
1. Make sure you selected the steg file (the output from hiding operation)
2. Verify the file wasn't modified by other software
3. Check you're using a file created by NigudhaX

### Problem: Application doesn't start

**Cause:** Missing dependencies or Python issue.

**Solution:**
1. Reinstall dependencies: `pip install -r steg_tool/requirements.txt`
2. Check Python version: `python --version` (should be 3.8+)
3. Try: `python3 -m steg_tool.app` instead

### Problem: File size too large

**Cause:** Payload is very large, creating a noticeably big steg file.

**Solution:**
1. Use a larger carrier file
2. Compress payload first (ZIP with maximum compression)
3. Consider splitting into multiple steg files

---

## Tips & Best Practices

### Security Tips

1. **Always Use Passwords**
   - Even if file seems unimportant
   - Passwords add strong encryption layer
   - Use unique passwords for different files

2. **Choose Appropriate Carriers**
   - Use common file types (photos, music)
   - Don't use tiny images for large payloads
   - Match carrier to context (vacation photo for travel docs)

3. **Be Mindful of File Sizes**
   - Steg file = Carrier size + Payload size + Small overhead
   - A 1MB photo with 5MB payload = ~6MB steg file
   - Large size increases may raise suspicion

4. **Don't Modify Steg Files**
   - Don't edit, crop, or compress steg files
   - Any modification may corrupt hidden data
   - Keep originals as backup

### Practical Tips

1. **Test First**
   - Hide a test file before important data
   - Verify extraction works
   - Confirm password is correct

2. **Keep Backups**
   - Always keep original files
   - Save steg files securely
   - Document passwords safely (password manager)

3. **Organize Your Workflow**
   - Create a workflow folder structure:
     ```
     steganography/
     ├── carriers/        (source images/audio)
     ├── payloads/        (files to hide)
     ├── output/          (steg files)
     └── extracted/       (retrieved files)
     ```

4. **Naming Conventions**
   - Keep steg files naturally named
   - `vacation_2024.jpg` is better than `hidden_secret.jpg`
   - Blend in with other files

### Educational Tips

1. **Understand the Limitations**
   - This is not pixel-level steganography
   - Data is appended, not embedded
   - File size analysis can reveal hidden data

2. **Experiment Safely**
   - Try different file types
   - Test with various sizes
   - Learn by doing

3. **Read the Technical Documentation**
   - Understand the format specification
   - Learn about encryption methods
   - Study the source code

---

## Quick Reference Card

### Hide File
```
1. Launch: python -m steg_tool.app
2. Tab: "Encrypt / Hide"
3. Select: Carrier file (image/audio/video)
4. Select: Payload file (anything to hide)
5. Optional: Set output path
6. Optional: Enter password
7. Click: "Hide File"
```

### Extract File
```
1. Launch: python -m steg_tool.app
2. Tab: "Decrypt / Extract"
3. Select: Steg file (file with hidden data)
4. Select: Destination directory
5. Optional: Enter password (if was used)
6. Click: "Extract Hidden File"
```

### Command Line Quick Start
```bash
# Run application
python -m steg_tool.app

# Install dependencies
pip install -r steg_tool/requirements.txt

# Build standalone executable (optional)
pyinstaller -F -w steg_tool/app.py -n StegTool
```

---

## Frequently Asked Questions

**Q: Can anyone extract the hidden file?**
A: Without a password, technically yes (with NigudhaX). With a password, they need both NigudhaX and the correct password.

**Q: Does hiding damage the carrier file?**
A: No! The carrier remains fully functional. Images display normally, audio plays normally, etc.

**Q: What's the maximum file size I can hide?**
A: Limited only by your disk space. However, keep in mind the steg file will be carrier + payload size.

**Q: Can I hide a file in a steg file?**
A: Yes! You can chain operations (hide in hidden files). See Advanced Usage section.

**Q: Is this detectable by antivirus software?**
A: The application itself is safe. Steg files appear as normal files to antivirus software.

**Q: Can I share steg files online?**
A: Yes! Just share like any normal file. Remember to share the password separately and securely.

---

## Getting Help

**Need More Help?**
- Check the main README.md for technical details
- Open an issue on GitHub
- Review the source code in `steg_tool/` directory

**Contributing:**
- Found a bug? Report it!
- Have a feature idea? Suggest it!
- Want to improve docs? Submit a PR!

---

**Happy Hiding with NigudhaX! 🎭**

*Remember: Use responsibly and ethically. This tool is for educational purposes and legitimate privacy needs.*
