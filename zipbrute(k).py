import pyzipper
import argparse

parser = argparse.ArgumentParser(description='\n usage: python zipbrute.py -z <ziparchive.zip> -p <passwordfile.txt>')
parser.add_argument('-z', dest='ziparchive', help='specify zip archive file')
parser.add_argument('-p', dest='passwordfile', help='specify password file')
parsed_args = parser.parse_args()

try:
    ziparchive = pyzipper.AESZipFile(parsed_args.ziparchive)
    passwordfile = parsed_args.passwordfile
    foundpass = ""
except:
    print(parser.description)
    exit(0)

with open(passwordfile, 'r') as f:
    for line in f:
        password = line.strip("\n")
        password = password.encode('utf-8')

        try:
            ziparchive.extractall(pwd=password)
            print("\nPassword found: " + password.decode())
            foundpass = password.decode()
            break
        except:
            pass

if foundpass == "":
    print("\nPassword not found. Try a bigger password file.")
