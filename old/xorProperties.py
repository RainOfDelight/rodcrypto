#import my custom library

KEY1    = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY21   = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY32   = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FLAG132 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key1 = hexStrToIntArr(KEY1)
print("key1" , len(key1), key1)

key21 = hexStrToIntArr(KEY21)
print("key21" , len(key21), key21)

key2 = intArr1xorintArr2(key1, key21)
print("key2" , len(key2), key2)

key32 = hexStrToIntArr(KEY32)
key3 = intArr1xorintArr2(key32, key2)
flagish = hexStrToIntArr(FLAG132)
for index in range(0, len(flagish)):
    print(chr(flagish[index]^key1[index]^key2[index]^key3[index]), end="")

flag32 = intArr1xorintArr2(flagish, key1)
flag3 = intArr1xorintArr2(flag32, key2)
flag = intArr1xorintArr2(flag3, key3)
print(intArrToString(flag))
