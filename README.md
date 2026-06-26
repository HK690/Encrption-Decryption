# 🔐 Python Encryption & Decryption Tool

A simple command-line **Encryption & Decryption Tool** built with **Python** using the **Cryptography (Fernet)** library.

This project allows users to securely encrypt and decrypt text using a symmetric encryption key. If no encryption key exists, the program automatically generates one and stores it in a `key.txt` file for future use.

---

## ✨ Features

* 🔑 Automatically generates an encryption key on first run.
* 💾 Saves the key locally in `key.txt`.
* 🔒 Encrypts plain text using Fernet symmetric encryption.
* 🔓 Decrypts previously encrypted text.
* ⚠️ Handles invalid encrypted data gracefully.
* 📋 Easy-to-use menu-driven command-line interface.

---

## 🛠️ Technologies Used

* Python 3.x
* Cryptography Library (`cryptography`)
* Fernet Symmetric Encryption

---

## 📂 Project Structure

```
Encryption-Decryption/
│
├── main.py          # Main program
├── key.txt          # Automatically generated encryption key
└── README.md
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/HK690/Encryption-Decryption.git
cd Encryption-Decryption
```

### 2. (Optional) Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required package

```bash
pip install cryptography
```

---

## ▶️ Running the Program

```bash
python main.py
```

---

## 📖 How It Works

When the application starts:

* Checks whether `key.txt` exists.
* If not, a new encryption key is generated automatically.
* The user can then:

  * Encrypt text
  * Decrypt text
  * Exit the application

---

## 💻 Example

```
Welcome to the Encryption/Decryption Program!

Menu:
1. Encrypt
2. Decrypt
3. Exit

Enter your choice: 1

Enter the data to encrypt:
Hello World

Encrypted data:
gAAAAABmxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Decrypting the encrypted text:

```
Menu:
1. Encrypt
2. Decrypt
3. Exit

Enter your choice: 2

Enter the data to decrypt:
gAAAAABmxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Decrypted data:
Hello World
```

---

## 🔒 About Fernet Encryption

This project uses **Fernet**, a symmetric encryption method provided by the Python `cryptography` library.

Fernet guarantees:

* Confidentiality
* Integrity
* Authentication

Only someone with the same generated key can successfully decrypt the encrypted data.

---

## 📌 Future Improvements

* Encrypt and decrypt files
* GUI version using Tkinter or PyQt
* Password-protected encryption key
* Multiple key management
* Save encrypted messages to a file

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **Harshal Kapse**.
