import base64
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive encryption key from password using PBKDF2"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_data(data: str, password: str) -> tuple[bytes, bytes]:
    """Encrypt data returning (ciphertext, salt)"""
    salt = os.urandom(16)
    key = derive_key(password, salt)
    f = Fernet(key)
    return f.encrypt(data.encode()), salt

def decrypt_data(encrypted_data: bytes, password: str, salt: bytes) -> str:
    """Decrypt data using password and salt"""
    key = derive_key(password, salt)
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()