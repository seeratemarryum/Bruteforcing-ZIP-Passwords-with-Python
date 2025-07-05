# 🔐 ZIP Password Brute Forcer (Python)

A simple Python script to brute-force password-protected `.zip` files using a list of potential passwords.


## 📁 Files in This Project

- `zipbrute.py` — Main Python script
- `archive.zip` — Password-protected ZIP file (target)
- `passlist.txt` — Wordlist containing possible passwords
- `secret.txt` — (Optional) The original file used to create `archive.zip`


## ⚙️ Requirements

- Python 3.6+
- Basic terminal or command-line access

> ❗ This version supports **ZipCrypto-encrypted ZIP files only** (not AES). If using AES-encrypted ZIPs (e.g., from WinRAR), see the pyzipper version.



## 🖥️ Running on **Windows**

### Step 1: Install Python
- Download from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"


### Step 2: Prepare Files
Put all of the following in the same folder (e.g., `path to\Bruteforcing ZIP Passwords`):

- `zipbrute.py`
- `archive.zip`
- `passlist.txt`

> ⚠️ Make sure the ZIP file is encrypted with **ZipCrypto**, not AES.  
> Use **7-Zip**, not WinRAR.  
> In 7-Zip:  
> ➤ Archive format: `zip`  
> ➤ Encryption method: `ZipCrypto`


###  Step 3: Run the Script

1. Open Command Prompt
2. Navigate to the project folder:
   ```cmd
   E:
   cd "path to\Bruteforcing ZIP Passwords"
Run the script:
   ```cmd
    python zipbrute.py -z archive.zip -p passlist.txt
```

##  Running on **Kali Linux**

### ✅ Step 1: Set Up a Virtual Environment (Recommended)

```bash
python3 -m venv zipenv
source zipenv/bin/activate
```

## Step 2: Install pyzipper
```bash
pip install pyzipper
```

## Step 3: Create a Password-Protected ZIP File
```bash
zip -e archive.zip secret.txt #Set a known password (e.g. secret123)
```

## Step 4: Run the script:
```bash
python3 zipbrute.py -z archive.zip -p passlist.txt
```
