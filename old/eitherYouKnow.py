from usefulfunc import *

encrypted   = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
flag        = "crypto{1B"
key         = "myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey"
a = hexStrToIntArr(encrypted)


c = intArr1xorintArr2(a, strToIntArr(key))
print(intArrToString(c))

finished = True
bruteforcing = len(flag)
while not finished:
    print("Guessing char ",str(bruteforcing), " - ",  flag, "->(?)")
    for integer in range(65, 125):
        potentialFlag = strToIntArr(flag+chr(integer))
        c = intArr1xorintArr2(a, potentialFlag)
        if 65<c[bruteforcing]<125:
            print(intArrToString(potentialFlag)[0:bruteforcing+1], intArrToString(c)[0:bruteforcing+1])
            #good = input("Is it good?")
            #if good == 'y':
                #flag =potentialFlag
                #bruteforcing = bruteforcing + 1
                #break


