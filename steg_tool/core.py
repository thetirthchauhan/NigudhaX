import os, struct, hashlib, secrets
from typing import Optional, Tuple
from .format_spec import MAGIC, VERSION, FLAG_ENCRYPTED, StegFormatError

try:
    from nacl.secret import SecretBox
    from nacl.hash import blake2b
    from nacl.encoding import RawEncoder
    HAVE_NACL = True
except Exception:
    HAVE_NACL = False

HEADER_STRUCT = struct.Struct('<8sB B Q H')  # MAGIC, VERSION, FLAGS, orig_size, name_len

# After name: payload_size (Q), sha256 (32), [nonce_len( B ), nonce(var)], encrypted_data


def kdf(password: str) -> bytes:
    # Simple KDF (not memory-hard) for demo; could be replaced with scrypt/argon2
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'STEGTOOL-SALT', 200_000, dklen=32)


def simple_xor(data: bytes, key: bytes) -> bytes:
    kl = len(key)
    return bytes(b ^ key[i % kl] for i, b in enumerate(data))


def pack(carrier_path: str, payload_path: str, out_path: Optional[str] = None, password: Optional[str] = None) -> str:
    """Embed payload into carrier by appending a custom structured blob.

    If out_path is:
      - None: create <carrier_root>_packed<carrier_ext>
      - A directory: create file inside directory with carrier base name + '_packed' + carrier ext
      - A path without extension: append carrier extension automatically (so image still opens)
      - A path with different extension: override to carrier extension to ensure viewer compatibility
    """
    carrier_root, carrier_ext = os.path.splitext(carrier_path)
    if out_path is None or not out_path.strip():
        out_path = carrier_root + '_packed' + carrier_ext
    else:
        out_path = os.path.abspath(out_path)
        # If user passed a directory, drop file inside it
        if os.path.isdir(out_path) or out_path.endswith(os.sep):
            base_name = os.path.basename(carrier_root) + '_packed' + carrier_ext
            out_path = os.path.join(out_path, base_name)
        else:
            root, ext = os.path.splitext(out_path)
            if ext == '':
                # No extension provided -> use carrier ext
                out_path = out_path + carrier_ext
            elif ext.lower() != carrier_ext.lower():
                # Force carrier extension to keep file type valid
                out_path = root + carrier_ext
    with open(carrier_path, 'rb') as f: carrier_bytes = f.read()
    with open(payload_path, 'rb') as f: payload_bytes = f.read()
    payload_name = os.path.basename(payload_path).encode('utf-8')
    sha256 = hashlib.sha256(payload_bytes).digest()

    flags = 0
    enc_payload: bytes
    nonce = b''
    if password:
        flags |= FLAG_ENCRYPTED
        key = kdf(password)
        if HAVE_NACL:
            box = SecretBox(key)
            nonce = secrets.token_bytes(SecretBox.NONCE_SIZE)
            enc_payload = box.encrypt(payload_bytes, nonce).ciphertext
        else:
            enc_payload = simple_xor(payload_bytes, key)
    else:
        enc_payload = payload_bytes

    header = HEADER_STRUCT.pack(MAGIC, VERSION, flags, len(carrier_bytes), len(payload_name))
    rest = struct.pack('<Q', len(payload_bytes)) + sha256
    if flags & FLAG_ENCRYPTED:
        rest += struct.pack('B', len(nonce)) + nonce
    blob = header + payload_name + rest + enc_payload
    with open(out_path, 'wb') as f:
        f.write(carrier_bytes)
        f.write(blob)
    return out_path


def find_and_unpack(steg_path: str, out_dir: str, password: Optional[str] = None) -> str:
    with open(steg_path, 'rb') as f:
        data = f.read()
    # Scan from end for MAGIC (simple approach: assume appended once)
    idx = data.rfind(MAGIC)
    if idx == -1:
        raise StegFormatError('No hidden data found')
    # Parse header
    if len(data) < idx + HEADER_STRUCT.size:
        raise StegFormatError('Truncated header')
    magic, version, flags, orig_size, name_len = HEADER_STRUCT.unpack_from(data, idx)
    if magic != MAGIC:
        raise StegFormatError('Magic mismatch')
    if version != VERSION:
        raise StegFormatError('Unsupported version')
    cursor = idx + HEADER_STRUCT.size
    payload_name = data[cursor:cursor+name_len]; cursor += name_len
    payload_size = struct.unpack_from('<Q', data, cursor)[0]; cursor += 8
    sha256 = data[cursor:cursor+32]; cursor += 32
    nonce = b''
    if flags & FLAG_ENCRYPTED:
        nonce_len = data[cursor]; cursor += 1
        nonce = data[cursor:cursor+nonce_len]; cursor += nonce_len
    enc_payload = data[cursor:cursor + (len(data) - cursor)]

    if flags & FLAG_ENCRYPTED:
        if not password:
            raise StegFormatError('Password required')
        key = kdf(password)
        if HAVE_NACL:
            box = SecretBox(key)
            payload_bytes = box.decrypt(nonce + enc_payload)  # SecretBox expects nonce + ciphertext
        else:
            payload_bytes = simple_xor(enc_payload, key)
    else:
        payload_bytes = enc_payload

    if len(payload_bytes) != payload_size:
        raise StegFormatError('Size mismatch')
    if hashlib.sha256(payload_bytes).digest() != sha256:
        raise StegFormatError('Integrity check failed')
    out_name = payload_name.decode('utf-8', 'replace')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, out_name)
    with open(out_path, 'wb') as f:
        f.write(payload_bytes)
    return out_path
