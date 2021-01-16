#!/usr/bin/env python3
import sys
"""
if len(sys.argv) != 4:
    print("Usage: "+sys.argv[0]+" message_file key encrypted")
    sys.exit(1)
"""

def encrypt(message, key):
    with open(message, 'rb') as content_file:
        content = content_file.read()
    if len(content) != 256:
        raise Exception('This is a block cipher, messages have to be exactly 256 bytes long')
    ciphertext = list(' ' * 256)
    for i in range(0,256):
        new_pos = (3**(key+i)) % 257
        ciphertext[new_pos-1] = ((content[i])^i)^(new_pos-1)    # il dato e' xorato con posizione iniziale e posizione finale
    return bytes(ciphertext)

def decrypt(message):
    with open(message, 'rb') as content_file:
        cipherText = content_file.read()
    if len(cipherText) != 256:
        raise Exception('This is a block cipher, messages have to be exactly 256 bytes long')
    sequence= {}     #la sequenza si ripetera dopo 256 valori, sequence[256] = sequence[0]
    for i in range(0,560):
        sequence[i]=((3**(i)) % 257) -1
    print(sequence)

    plaintext = list(' ' * 256)    #create empty list where I will save the result

    #go throuch all the possibilities of encripting messages
    for shift in range(0,256):
        #creating subsequence
        subsequence = {}
        for i in range(0,256):
            subsequence[i]=sequence[shift+i]

        print(subsequence)
        for cipherIndex in range(0, 256):
            encByte = cipherText[cipherIndex]
            cameFrom = [k for (k, v) in subsequence.items() if v == cipherIndex]
            cameFrom = cameFrom[0]
            decrypted = encByte ^ cipherIndex ^ cameFrom
            plaintext[cameFrom] = decrypted
        print(bytes(plaintext))

def test(key):
    for i in range(0, 17):
        print((3 ** (key + i)) % 17, " vs ", (3 ** (i)) % 17)

decrypt('Log Caesar encrypted.txt')

"""
ciphertext = encrypt(sys.argv[1],int(sys.argv[2]))
with open(sys.argv[3],'wb') as encryped_file:
    encryped_file.write(ciphertext)
"""

