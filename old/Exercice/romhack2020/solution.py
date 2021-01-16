import base64
import cryptonita
import string

def bxor(b1, b2): # use xor for bytes
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return result

def testKeyForTower(key):
    print("TRYING SPECIFIC KEY")
    for index in range(0, len(fromTower)):
        res=bxor(key, fromTower[index])
        print(res)

def testKeyForPlane(key):
    print("TRYING SPECIFIC KEY")
    for index in range(0, len(fromPlane)):
        res = bxor(key, fromPlane[index])
        print(res)


def SearchPatternInFromPlane(bytePattern):
    for first in range(0, len(fromPlane)):
        for second in range(first, len(fromPlane)):
            if first == second:
                continue
            if len(fromPlane[first]) < len(fromPlane[second]):
                shortest = len(fromPlane[first])
            else:
                shortest = len(fromPlane[second])

            ris = bxor(fromPlane[first], fromPlane[second])
            for i in range(0, shortest - len(bytePattern)):
                forged = b"\x00" * i + bytePattern
                result = bxor(ris, forged)[-5:]
                if result[0] in range(32, 126) and result[1] in range(32, 126) and result[2] in range(32, 126) and \
                        result[3] in range(32, 126):
                    print("first=", first, "second=", second, i, "bytes with x00 then ", result)

allowedCharacters=[97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,32,46,33]
def SearchPatternInFromTower(bytePattern):
    for first in range(0, len(fromTower)):
        for second in range(first, len(fromTower)):
            if first == second:
                continue
            if len(fromTower[first]) < len(fromTower[second]):
                shortest = len(fromTower[first])
            else:
                shortest = len(fromTower[second])

            ris = bxor(fromTower[first], fromTower[second])
            for i in range(0, shortest - 5):
                forged = b"\x00" * i + bytePattern
                result = bxor(ris, forged)[-5:]
                if result[0] in allowedCharacters and result[1] in allowedCharacters and result[2] in allowedCharacters and result[3] in allowedCharacters:
                    print("first=", first, "second=", second, i, "bytes with x00 then ", result)


printable_chars = range(33,126)
allMessages="""3BayjKtNc6gOZQvTZgfsy80N5Yi3TWW3H2gbljENoozAFrLJtBhzr1tlAJ12B76M3xzlmrECZasfKRiSeBbz5Pw=
9y2tX7VC8Oe/ngmZefWNlepoqhasT7WovM0JmHG0nZXiKadfqFm1rrSJGJZ9+pCE62aBCw==
wVmkhPkdYqIPfRbTYhe+yYgOoMm9AjCpFH1Pm3AUqYzcEaDJvxh1q1tvAIExFqTN3FiHkg==
/Ce5GrMK4a+7mV2SYeDZhOYtrBrhQ+bnu80bkXn9lYmuJ7hfp0XtoqnNHoJ754qZ4C/+C6lPtbO7lRSHde3XmL0=
/SesDbgK/LP6gRKff+fZnOcju1+2QvSz+p4UgivLig==
wQ3lhbYCe7RbZQaYdEKtjMocpIe7DHfnGGEOmmNMop8=
7ySsFqZC4eeznl2EfPGLla4ktxSkCvTntowLkTT4mJ3+aL8RpQrwr/qMXYN97NmA7yu1X65f4eeuhRiCcbSNn+F36hI=
yRu2hrUYZKIXcEPTdQu/z8dZp4i1ATCmCCkYln0O4tqb
zxaxybgDaecLewqeeBehjMsWo4+8CDCyCykbm3QQqZPaJg==
4SD+Ha5Tta76mhSDfLSQ0OYpul+gCvayqs0SljTki5XjIasS4BnK
zBy1iKsZZbUeKQeSZwfszYgeqoa9TX6uHGEb02UNu8naVeWA+Q91s1twAIZjQq/Dzh+gjPkEY+cZbBuHdBDs2MAYq8m4BGK3F2gBljEBo8rNHOub6g==
4SD+FrVZtab6w1PeNPqchus6/hKoRPHr+oRdk3X62Z7hPP4MoFO1rq7DFsM=
6T2nDOFP46KolBKecbSQg648vxOqQ/ug+owJ0GD8nND9KbMa4V78qr/BXZk09ZTQ+imyFKhE8ueugl2EfOacla4nqhekWLWktYMJgnv4lZX8O/4KsQr9oqiIUdB9tI6Z4iT+HKBG+eejggjebeeN
ygyxybBNfqIebU+HfkK4zcQS5Z22TWmoDicagA==
+S2yE+FD8+ejggjQfPWPla4psF+kR/C1vYgTk220npn4Lf4SpAr057mMEZw65srE
xwmgh/kef6oeKRyWchaj3ttX9g==
9y2/F+0K4a+/nxjRNOORia4ssRHmXrW+tZhdk3X4ldDgLalfuEXnrPqOGJ5g8YvQ7ya6X7VP+av6mRWVebSNn64ssV+1QvSz5YAA"""
arrayAllMessages = allMessages.split("\n")
arrayAllMessagesInBytes = []
for mex in arrayAllMessages:
    mexInBytes = mex.encode()
    arrayAllMessagesInBytes.append(base64.decodebytes(mexInBytes))


fromTower=[]
fromPlane=[]
#message 0 will be attributed to the TOWER, i dont knwo if its like that or no
#messages belongoing to the first sender are : 1,3,6,8,9,11,14,16
for i in [1,3,6,8,9,11,14,16]:
    fromTower.append(base64.b64decode(arrayAllMessages[i-1]))
for i in [0,2,4,5,7,10,12,13,15,17]:
    fromPlane.append(base64.b64decode(arrayAllMessages[i-1]))


first=0
second=1
pad=31
print("Possible keys, (last 5 bytes)")
print(bxor(b"\x00"*pad+b" the ", fromTower[first]))
print(bxor(b"\x00"*pad+b" the ", fromTower[second]))


planeKey =      b"\xaeH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0"
planeKey =      b"\xaeH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8eH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8eH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8eH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\xaeH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8eH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8eH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8eH\xde\x7f\xc1*\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0\x8e\x48\xde\x7f\xc1\x2a\x95\xc7\xda\xed\x7d\xf0\x14\x94\xf9\xf0"
testKeyForPlane(planeKey)
#SearchPatternInFromPlane(b" plane ")

"""
towerKey
\xac\xa8y\xc5\xe9
"""
towerKey=b"\xa8y\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79"
#towerKey=b"\xa8y\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8y\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\xa8\x79\xc5\xe9\xd9\x6d\x10\xc7\x7b\x09\x6f\xf3\x11\x62\xcc\xac\x00"
testKeyForTower(towerKey)

#bruteforcing all bytes:
def bruteforceByte(knownText):
    for i in range(0,256):
        payload = knownText+i.to_bytes(1,'big')
        results=[]
        for index in range(0, len(fromTower)):
            results.append(bxor(payload, fromTower[index]))
        printable = True
        for res in results:
            if res[len(knownText)] not in range(25,125):
                printable = False

        if printable:
            print(i, "\n")
            for result in results:
                print(result)
            print("\n")
#bruteforceByte(b"")

#SearchPatternInFromTower(b" the ")


