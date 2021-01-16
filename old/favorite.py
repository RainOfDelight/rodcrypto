from usefulfunc import *

crypted = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'


hexarr=hexStrToHexArr(crypted)
print("HEXARR", hexarr)

intarr=hexArrToIntArr(hexarr)
print("INTARR", intarr)

stringozza= intArrToString(intarr)
print("STRINGA INIZIALE -> ", stringozza)

for index in range(0, 255):
    xored = xored=intArrXorInt(intarr, index)
    print(index, intArrToString(xored))



