import zlib
import requests
import binascii

#   This script bture forces the flag 1 character at the time. You have to look at which output is the shortest
#   Since that is the one which is correct. If I prepend a string that is same as part of the flag, the encription
#   return a smaller value, so even if encrypted, it will still be shorter

flag=b"crypto{CRIME_571ll_p4y5}"  #at the beginning flag was equal to "crypto{" because I know that string was present 100%
payload=bytearray
payloads=b"qwertyuiopasdfghjlkzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[];',./<>?:{}\"|1234567890-_!#$%^&*()`~=+!?"
tries = {}
for i in  payloads:
    basic = (flag + i.to_bytes(1, 'big'))
    tries[basic]=[]
    #for num in range(1,4):
    payload=basic*4
    strpayload = binascii.hexlify(payload).decode()
    response = requests.get("http://aes.cryptohack.org/ctrime/encrypt/"+strpayload)
    if response.status_code != 200:
        print("NON 200")
        exit
    responseLength = len(response.content)

    tries[basic]=responseLength

print(sorted( ((v,k) for k,v in tries.items())))    #print the dictionary sorted by values, so tha I know which one is shortest
"""        
sortedView = [ (v,k) for k,v in tries.iteritems() ]
sortedView.sort() # natively sort tuples by first element
for v,k in sortedView:
    print ("%s: %d" % (k,v))
"""