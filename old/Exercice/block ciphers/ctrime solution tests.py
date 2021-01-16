import zlib
import requests
import binascii

flag = b"crypto{laladani}"
str = b"crypto{laladani"
print(len(zlib.compress(str+flag)))
print(len(zlib.compress(str*2+flag)))
print(len(zlib.compress(str*3+flag)))
print(len(zlib.compress(str*4+flag)))
print(len(zlib.compress(str*5+flag)))
print(len(zlib.compress(str*6+flag)))

