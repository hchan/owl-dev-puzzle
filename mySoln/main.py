import base64
from caesarcipher import CaesarCipher
import re

file = open("ENCRYPTED", "r") # ENCRYPTED is the original Hootsuite puzzle that bigger brother found on a Hootsuite USB
contents = file.read()
file.close() # just being tidy and closing the file object
decoded = base64.b64decode(contents)
upper_chars = re.sub(r'[^A-Z]', '',  decoded.decode('utf-8')) # strip out all characters that are not upper case
cipher = CaesarCipher(upper_chars) # The Hootsuite person who wrote this puzzle, didn't make this simple!
print(cipher.cracked)
