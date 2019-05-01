import base64
import re
from caesarcipher import CaesarCipher

file = open("ENCRYPTED", "r").read()

decoded = base64.b64decode(file)

upper_chars = []

for c in decoded:
  if c.isupper():
    upper_chars.append(c)


cipher = CaesarCipher(upper_chars)
cipher.cracked
print(cipher.cracked)

