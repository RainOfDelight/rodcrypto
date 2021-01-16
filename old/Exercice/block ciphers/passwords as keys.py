from Crypto.Cipher import AES
import hashlib
import random

#@chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash): #both ciphertext and password_hash must be in hex form
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted


#@chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}


FLAG = "?"
ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"


w = open("lala", 'a')

with open("words") as f:
    for password in f:
        password = password.strip()     # PERCHE QUANDO LEGGEVO LA RIGA LEGGEVO ANCHE L'ANDATA A CAPO FINALE!!
        KEY = hashlib.md5(password.encode()).digest().hex()
        result = decrypt(ciphertext, KEY)
        try:
            res=result.decode()
            print(res)
        except Exception as e:
            pass


