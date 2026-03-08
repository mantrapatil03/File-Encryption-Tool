<h1 align="center">File Encryption Tool (AES-256 Secure Encryption)</h1>

<p align="center">
  <b>A secure command-line file encryption tool built using Python and Cryptography</b><br>
  Encrypt and decrypt files safely using password-based AES-256 encryption.
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python">
  </a>
  <img src="https://img.shields.io/badge/Encryption-AES--256-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Security-PBKDF2-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-blue?style=for-the-badge">
</p>

---

# Overview

**File Encryption Tool CLI** is a simple yet powerful Python command-line tool that allows users to **securely encrypt and decrypt files using a password**.

It uses **PBKDF2 key derivation** and **AES-256 encryption via Fernet**, ensuring that files remain protected from unauthorized access.

This tool is ideal for:

- protecting sensitive files
- learning cryptography concepts
- cybersecurity projects
- secure file sharing

---

# Features

✅ **AES-256 encryption** for strong file protection  
✅ **Password-based encryption** using PBKDF2  
✅ **Secure salt generation** for every encryption  
✅ Encrypt **any type of file** (text, image, pdf, etc.)  
✅ Simple **command-line interface**  
✅ Cross-platform support (Linux, Windows, macOS)  
✅ Safe error handling for incorrect passwords  
✅ Lightweight and easy to use  

---

# Repository Structure
```
file-encryption-tool/
│
├── encryptor/
│ ├── init.py
│ ├── crypto_utils.py       # Encryption & decryption logic
│ └── cli.py                # Command line interface
│
├── examples/
│ └── sample.txt            # Example file for testing
│
├── main.py                 # Project entry point
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
```


---

# Installation

## 1️⃣ Clone the repository
```
git clone https://github.com/mantrapatil03/File-Encryption-Tool.git
```
```
cd File-Encryption-Tool
```

<h2 align="center"> OR </h2>

Download the ZIP and extract it manually.

---

## 2️⃣ Create Virtual Environment (Recommended)

### Linux / macOS
```
python3 -m venv venv
source venv/bin/activate
```

### Windows
```
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```


---

# Usage

## Encrypt a File
Encrypt
`python main.py encrypt examples/sample.txt -p mypassword`

Output:
`sample.txt.enc`

The encrypted file will be created in the same directory.

---

## Decrypt a File
Encrypt
`python main.py decrypt examples/sample.txt.enc -p mypassword`

Output:
`sample.txt.dec`

If the password is incorrect, the program will show:
**Incorrect password or corrupted file.**


---

# Example Workflow

Encrypt
`python main.py encrypt secret.txt -p strongpassword`

Output
`secret.txt.enc`

Decrypt
`python main.py decrypt secret.txt.enc -p strongpassword`

Output
`secret.txt.dec`


---

# Encryption Process

The tool secures files using the following steps:

1. **Generate random salt (16 bytes)**
2. **Derive secure key using PBKDF2**
3. **Encrypt file using Fernet (AES-256)**
4. **Store salt + encrypted data**

This ensures that:

- every encryption is unique
- brute-force attacks become difficult
- passwords cannot be reversed

---

# Security Technologies Used

| Technology | Purpose |
|--------|--------|
| **AES-256** | Strong symmetric encryption |
| **PBKDF2** | Secure password key derivation |
| **SHA256** | Cryptographic hashing |
| **Fernet** | Authenticated encryption |
| **Random Salt** | Prevents rainbow table attacks |

---

# Supported File Types

This tool can encrypt **any file format**, including:

- `.txt`
- `.pdf`
- `.jpg`
- `.png`
- `.zip`
- `.docx`
- `.mp4`
- etc.

Because the program works with **raw binary data**.

---

# Troubleshooting

### File Not Found
Ensure the correct file path is provided.

Example:
`python main.py encrypt examples/sample.txt -p password`


---

### Incorrect Password

You will see:

- Incorrect password or corrupted file.
- Make sure you use the **same password used during encryption**.

---

### Module Not Found Error

Install dependencies again:

```
pip install -r requirements.txt
```

---

# Developer Guide

Main Modules

| File | Description |
|-----|-------------|
| `main.py` | Entry point for running CLI |
| `cli.py` | Handles command line arguments |
| `crypto_utils.py` | Encryption & decryption logic |
| `requirements.txt` | Project dependencies |

---

# Contributing

Contributions are welcome!

If you'd like to improve the project:

1️⃣ Fork the repository  
2️⃣ Create a feature branch  
3️⃣ Write clean code and documentation  
4️⃣ Submit a pull request  

For major changes, open an issue first.

---

# License

This project is licensed under the **MIT License**.

---

# Author
**Mantra Patil**

Python Developer | Cybersecurity Enthusiast

---

<h2 align="center">💫 Thanks for Visiting! 💫</h2>

<p align="center">
<i>Made with ❤️ & Python</i><br><br>

<img src="https://img.shields.io/badge/Keep%20Coding-Python-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Star%20This%20Repo-GitHub-black?style=for-the-badge&logo=github" />

</p>

<p align="center">
🌟 <b>If you found this project helpful, please give it a star!</b> 🌟
</p>
