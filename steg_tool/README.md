# Steg Tool

Cross-platform Python GUI application for custom steganography (hiding any file inside a carrier media file like image/audio/video) with drag & drop support.

## Features
- Hide ("Encrypt") any file into a carrier file (.jpg/.png/.mp3/.mp4/any binary)
- Extract ("Decrypt") hidden file only with this tool via custom format & optional passphrase
- Drag & drop support for carrier and payload selection
- Integrity verification (SHA256)
- Simple XOR+ChaCha20 (PyNaCl fallback) hybrid encryption (if password provided) else just packaging
- Custom magic header prevents accidental extraction by other tools

## Custom Container Format
```
MAGIC: 8 bytes  (b'STEGTOOL')
VERSION: 1 byte (0x01)
FLAGS: 1 byte   (bit0 = encrypted?)
ORIG_CARRIER_SIZE: 8 bytes unsigned little-endian
PAYLOAD_NAME_LEN: 2 bytes unsigned little-endian
PAYLOAD_NAME: variable (utf-8)
PAYLOAD_SIZE: 8 bytes unsigned little-endian
PAYLOAD_SHA256: 32 bytes
NONCE_LEN: 1 byte (only if encrypted)
NONCE: variable
CIPHERTEXT/PAYLOAD_BYTES: variable
```
Data appended to end of carrier file.

## Dependencies
- Python >= 3.8
- tkinter (bundled) for GUI
- pynacl (optional, for stronger encryption) fallback to pure XOR

## Run
```
python -m steg_tool.app
```

## Packaging
Use PyInstaller (not included here) to build platform binaries.

## Security Note
This is not industrial-grade steganography (does not modify pixels/frames) but container appending with light encryption. Suitable for casual concealment, not for high-security environments.
