from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description='\n using: Bruteforcing ZIP Passwords.py -z <ziparchive.zip> -p <passwordfile.txt>')
parser.add_argument('-z', dest='ziparchive', help='specify zip archive file')
parser.add_argument('-p', dest='passwordfile', help='specify password file')
parsed_args = parser.parse_args()

try:
    ziparchive = ZipFile(parsed_args.ziparchive)
    passwordfile = parsed_args.passwordfile
    foundpass = ""
except:
    print(parser.description)
    exit(0)

with open(passwordfile, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        password = line.strip().encode('utf-8')

        try:
            # ──> **FIX 1:** call extractall WITHOUT assigning its return value
            ziparchive.extractall(pwd=password)

            # ──> **FIX 2:** print correctly, mark success, and break
            print("\nPassword found:", password.decode())
            foundpass = password.decode()
            break
        except RuntimeError:
            pass

if foundpass == "":
    print("\nPassword not found. Try a bigger password file.")
