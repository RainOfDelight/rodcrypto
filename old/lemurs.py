from usefulfunc import *

#This one just XORS the files, making them unreadable by the OS

stringFlag= "7ae18c704272532658c10b5faad06d74"
stringLemur = "ed66878c338e662d3473f0d98eedbd0d"
print(intArrToString(hexStrToIntArr(stringFlag)))
print(intArrToString(hexStrToIntArr(stringLemur)))
print(intArrToString(intArr1xorintArr2(hexStrToIntArr(stringFlag),hexStrToIntArr(stringLemur))))

with open("other/lemur_ed66878c338e662d3473f0d98eedbd0d.png", "rb") as image:
  f = image.read()
  lemurBytes = bytearray(f)

with open("other/flag_7ae18c704272532658c10b5faad06d74.png", "rb") as image:
  f = image.read()
  flagBytes = bytearray(f)

print(len(flagBytes), len(lemurBytes))
print(flagBytes[0])

with open("other/xored.png", "wb") as image:
  allBytes = bytearray()
  for index in range(0, len(flagBytes)):
    allBytes.append(flagBytes[index] ^ lemurBytes[index])
  image.write(allBytes)