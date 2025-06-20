import json
import os
from pathlib import Path
from .crypto import encrypt_data, decrypt_data

VAULT_DIR = Path.home() / ".codevault"
VAULT_FILE = VAULT_DIR / "snippets.enc"
SALT_FILE = VAULT_DIR / "salt.bin"

def initialize_vault():
    """Create vault directory if needed"""
    VAULT_DIR.mkdir(exist_ok=True, mode=0o700)

def save_snippets(snippets: list, password: str):
    """Encrypt and save snippets"""
    encrypted, salt = encrypt_data(json.dumps(snippets), password)
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    os.chmod(VAULT_FILE, 0o600)
    os.chmod(SALT_FILE, 0o600)

def load_snippets(password: str) -> list:
    """Load and decrypt snippets"""
    if not VAULT_FILE.exists():
        return []
    
    with open(VAULT_FILE, "rb") as f:
        encrypted = f.read()
    with open(SALT_FILE, "rb") as f:
        salt = f.read()
    
    try:
        return json.loads(decrypt_data(encrypted, password, salt))
    except:
        raise ValueError("Invalid password or corrupted vault")