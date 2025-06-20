
# 🔐 CodeVault - Secure Your Code Snippets, the Terminal Way!

<p align="center">
  <img src="https://img.shields.io/github/license/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=brightgreen" />
  <img src="https://img.shields.io/github/forks/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=gray" />
  <img src="https://img.shields.io/github/stars/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=blue" />
  <img src="https://img.shields.io/github/issues/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=green" />
  <img src="https://img.shields.io/github/issues-pr/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=gold" />
</p>




**CodeVault** is a sleek, terminal-based utility built for the Windows CLI to help developers **securely store**, **encrypt**, **tag**, and **retrieve** reusable code snippets. With built-in search and categorization support, CodeVault keeps your snippets safe and at your fingertips. Perfect for productivity-driven developers and command-line enthusiasts!

## 🚀 Features

- **💾 Save snippets** with tags, titles and descriptions
- **🔐 AES-256 Encryption** for maximum security
- **🔍 Advanced search** by tags, titles or keywords
- **🏷️ Custom categorization** with unlimited tags
- **📁 Cross-platform** (Windows, Linux, macOS)
- **🧠 Simple commands** with intuitive interface


## Commands
```bash
# Add a new snippet
codevault add "snippet.py" --tags python fastapi --desc "API setup"

# Search your vault
codevault search python

# List all snippets
codevault list
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Quick Install
```bash
git clone https://github.com/HashSlap-Summer-of-Code/code-vault.git
cd code-vault
pip install -e .
```

### First-Time Setup
After installation, run any command to initialize your vault:
```bash
codevault list
```
You'll be prompted to create your master password - make it strong!

## 📖 Basic Usage

```bashg
# Add a code snippet
codevault add hello.py --tags python beginner --desc "Hello World"

# Search by tag
codevault search python

# Search by keyword
codevault search "hello world"

# List all snippets
codevault list

# Get detailed view
codevault view 1
```

## 📁 Repository Structure

```
code-vault/
├── codevault/
│   ├── __init__.py
│   ├── cli.py          # Command line interface
│   ├── crypto.py       # Encryption engine
│   └── storage.py      # Vault management
├── tests/              # Unit tests
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## 🔒 Security Model

Your snippets are protected with:
- AES-256 encryption using Fernet
- PBKDF2 key derivation with 390,000 iterations
- Unique cryptographic salt per vault
- Secure file permissions (600)
- Password never stored or transmitted

## 🧑‍💻 Contributing

We welcome contributors! Here's how to help:

1. **Report issues** or suggest features
2. **Fix bugs** - check our [Good First Issues](https://github.com/HashSlap-Summer-of-Code/code-vault/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
3. **Add features** - see our [Roadmap](#-roadmap)

**Contribution Workflow:**
```bash
# Fork and clone repository
git clone https://github.com/<your-username>/code-vault.git
cd code-vault

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

# Install dependencies
pip install -e .[dev]

# Run tests
pytest

# Create feature branch
git checkout -b feat/your-feature

# Commit and push changes
git commit -am "Add your feature"
git push origin feat/your-feature

# Open pull request
```
## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

💬 "Store it. Secure it. Retrieve it. CodeVault it!"
