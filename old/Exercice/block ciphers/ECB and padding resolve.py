from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
import codecs
hexlify = codecs.getencoder('hex')
#flag is 25 bytes long
#blocks are 16 bytes long aka 128bits

hexplaintext = ""


def findNextChar(knownText):
    hexplaintext = '00' * (31 - len(knownText))
    lookingforResponse = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/" + hexplaintext)
    if lookingforResponse.status_code == 200:
        lookingfor = lookingforResponse.content.decode()[15:79]
    else:
        raise Exception("Problem with the request, response code is not 200")
    for i in range(0,256):
        hexplaintext='00'*(31- len(knownText)) + knownText.encode("utf-8").hex() + str(hex(i))[2:].zfill(2)
        response = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/" + hexplaintext)
        lookingat = response.content.decode()[15:79]
        print("Hex sent ..." ,  hexplaintext[32:] , "->", lookingfor[32:], " =?= ", lookingat[32:], "FLAG = ", knownText)
        if(lookingat == lookingfor):
            knownText = knownText + chr(i)
            findNextChar(knownText)
            return

findNextChar('')