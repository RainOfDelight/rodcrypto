import requests



"""
http://aes.cryptohack.org/triple_des/encrypt/000000000000000100000000000000020000000000000000/13131313131313131313131313131313/


key = "000000000000000100000000000000020000000000000000"
plaintext = ""
url = "http://aes.cryptohack.org/triple_des/encrypt/"+key+"/"+plaintext+"/"
requests.get()

whatIWant= "4d20cd44fb6c37f513e082fc7e82190a5ea622fac7e3e674a9e0d027aaadaea9ea6eb1930af5b077"
"""

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad

import os
IV = b'\x8f\x88\x84\xc3d\xdd\xba\xb7'
FLAG = b"ciao"


#@chal.route('/triple_des/encrypt/<key>/<plaintext>/')
def encrypt(key, plaintext):
    try:
        key = bytes.fromhex(key)
        plaintext = bytes.fromhex(plaintext)
       # plaintext = xor(plaintext, IV)

        cipher = DES3.new(key, DES3.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        #ciphertext = xor(ciphertext, IV)

        return {"ciphertext": ciphertext.hex()}

    except ValueError as e:
        return {"error": str(e)}
