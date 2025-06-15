
# 🔐 CodeVault - Secure Your Code Snippets, the Terminal Way!

**CodeVault** is a sleek, terminal-based utility built for the Windows CLI to help developers **securely store**, **encrypt**, **tag**, and **retrieve** reusable code snippets. With built-in search and categorization support, CodeVault keeps your snippets safe and at your fingertips. Perfect for productivity-driven developers and command-line enthusiasts!

<p align="center">
  <img src="https://img.shields.io/github/license/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=brightgreen" />
  <img src="https://img.shields.io/github/forks/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=gray" />
  <img src="https://img.shields.io/github/stars/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=blue" />
  <img src="https://img.shields.io/github/issues/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=green" />
  <img src="https://img.shields.io/github/issues-pr/HashSlap-Summer-of-Code/code-vault?style=flat-square&color=gold" />
</p>

---

## 🚀 Features

- 💾 **Save** code snippets with tags and titles
- 🔐 **Encrypt** and store securely for privacy
- 🔍 **Search** by tags, titles, or keywords
- 🏷️ **Categorize** with custom labels
- 🧠 Simple commands like:

```bash
codevault add "snippet.py" --tag python --desc "FastAPI Setup"
codevault search python
codevault list
```

---

## 🛠️ Installation

> 📌 Windows CLI-only (for now)

```bash
git clone https://github.com/HashSlap-Summer-of-Code/code-vault.git
cd code-vault
python setup.py install
```

---

## 📁 Repository Structure

```bash
.
├── codevault/
│   ├── core.py
│   ├── cli.py
│   ├── encryption.py
│   └── utils.py
├── data/
│   └── snippets.json.enc
├── README.md
└── LICENSE
```

---

## 🧑‍💻 Contribution

* Raise an issue to suggest a feature or fix
* Fork the repo, make changes, and submit a PR!
* Follow best practices (PEP8, modular functions, etc.)

**Looking for good first issues?**
We welcome contributors to build new commands, improve encryption, or add export/import options.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

> 💬 *"Store it. Secure it. Retrieve it. CodeVault it!"*

---


