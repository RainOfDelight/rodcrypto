from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = '-'.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


print(encrypt_flag(FLAG))


cardinalityOfP= p-1
# I want to check if  a is a generator. If it is not, maybe I can find out whether b=0 or b=1, because if i dont have  generaotr, I might get some values out of the cycle
list = []
for index in range(1,100):
    result = pow(a,index,p)
    if result in list:
        print("Si ripete il ciclo dopo", len(list))
    else:
        list.append(result)
print(list)
