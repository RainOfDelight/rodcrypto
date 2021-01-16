#includes
from hashlib import sha256
import binascii

# Function to return gcd of a and b, also called, Euler algorithm
def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)

# function for extended Euclidean Algorithm
def EEA(a, b):

    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = EEA(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    # gcd is self explanatory
    # x*a + y*b will always be equal to gcd
    return gcd, x, y

# transform a hex string in a hex array, with a string made of 2 charactares
def hexStrToHexArr(hexStr):
    hexArr = []
    if(len(hexStr)%2 == 1):
        print("You entered dispari String")
        return False

    for index in range(0, len(hexStr), 2):
        hexArr.append(hexStr[index:index+2])
    return hexArr

# transform a hex string in an int array
def hexArrToIntArr(hexArr):
    intArr = []
    for elem in hexArr:
        intArr.append(int(elem, 16))
    return intArr

# self explenatory
def intArrToString(intArr):
    string=""
    for elem in intArr:
        string = string+chr(elem)
    return string

# xors each int int the array with a given number
def intArrXorInt(intArr, number):
    xoredArr = []
    for elem in intArr:
        xoredArr.append( elem ^ number)
    return xoredArr

# transform a string into an array of integers, each int corresponding to the ascii value of the character
def strToIntArr(stringa):
    intArr = []
    for elem in stringa:
        intArr.append(ord(elem))
    return intArr


def hexStrToIntArr(hexStr):
    return hexArrToIntArr(hexStrToHexArr(hexStr))

# this xors 2 int arrays until the smaller one finishes
def intArr1xorintArr2(arr1, arr2):
    result = []
    if len(arr1)<len(arr2):
        length = len(arr1)
    else:
        length = len(arr2)
    for index in range(0, length):
        result.append(arr1[index] ^ arr2[index])

    if True:
        if len(arr1)<len(arr2):
            result = result +arr2[len(arr1):]
        elif len(arr2)<len(arr1):
            result = result + arr1[len(arr2):]
    return result

def dictionaryPermutation(string, dict):
    #example of a dictionary, the unknown value is given by *, if you already know some values feed this function a dictionary
    #with those letters already set
    standardDictionary = {
        ' ': '*',
        'a': '*',
        'b': '*',
        'c': '*',
        'd': '*',
        'e': '*',
        'f': '*',
        'g': '*',
        'h': '*',
        'i': '*',
        'j': '*',
        'k': '*',
        'l': '*',
        'm': '*',
        'n': '*',
        'o': '*',
        'p': '*',
        'q': '*',
        'r': '*',
        's': '*',
        't': '*',
        'u': '*',
        'v': '*',
        'w': '*',
        'x': '*',
        'y': '*',
        'z': '*',
        'A': '*',
        'B': '*',
        'C': '*',
        'D': '*',
        'E': '*',
        'F': '*',
        'G': '*',
        'H': '*',
        'I': '*',
        'J': '*',
        'K': '*',
        'L': '*',
        'M': '*',
        'N': '*',
        'O': '*',
        'P': '*',
        'Q': '*',
        'R': '*',
        'S': '*',
        'T': '*',
        'U': '*',
        'V': '*',
        'W': '*',
        'X': '*',
        'Y': '*',
        'Z': '*',
        '0': '*',
        '1': '*',
        '2': '*',
        '3': '*',
        '4': '*',
        '5': '*',
        '6': '*',
        '7': '*',
        '8': '*',
        '9': '*'
    }

    result = ''
    for char in string:
        if char in dict:
            result += dict[char]
        else:
            result += '*'
    return result

def nToOneSubstitution(string, n, force=False):
    #substitute groups of n characters with one single letter inside the array subs. same groups of letters are mapped to same letter
    #force parameter is used to return a string even if not all the string has been translated, but only the first part
    arr = [string[i:i + n] for i in range(0, len(string), n)]
    subs = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOASDFGHJKLZXCVBNM'
    for i in range(0, len(arr)):
        if (len(arr[i]) > 1 and len(subs) > 0):
            target = arr[i]
            for j in range(i, len(arr)):
                if arr[j] == target:
                    arr[j] = subs[0]
            subs = subs[1:]
        else:
            if(len(subs)==0 and not force):
                raise Exception("numbers of single characters are insufficient to map every unique group of ", n, "letters")

    result = ''
    for a in arr:
        result = result + a
    return result

def sha256hashSearch(string, position, numberOfSearches):

    print("Searching for "+string)
    for i in range(0,numberOfSearches):
        hashed = sha256(str(i).encode()).hexdigest()
        if (position == 'start'):
            if (string == hashed[:len(string)]):
                return {'string':str(i), 'sha256hash':hashed}
        elif (position == 'end'):
            if (string == hashed[-len(string):]) :
                return {'string': str(i), 'sha256hash': hashed}
        else:
            if (string in hashed):
                return {'string':str(i), 'sha256hash':hashed}

def chineseReminder(congruences, modules):
    """
    x ≡ 2 mod 5
    x ≡ 3 mod 11
    x ≡ 5 mod 17
    Find the integer a such that x ≡ a mod 935
    [2,3,5] -> goes in the congruences array
    [5,11,17] -> goes in the modules array
    this program dont find the smalles x, it just finds an x
    """
    assert (len(congruences) == len(modules)), 'The length of the 2 input arrays must be the same'
    assert allPairsAreCoprime(modules), 'The modules are not coprime. For the Chinese Reminder to work they must be coprime'
    for elem in congruences:
        assert(isinstance(elem, int)), 'All the numbers in the congruences array must be integers'
    for elem in modules:
        assert(isinstance(elem, int)), 'All the numbers in the modules array must be integers'

    N = 1
    for mod in modules:
        N = N*mod

    x = 0
    for index in range(0, len(congruences)):
        x=x+ congruences[index]*N/modules[index]*pow(N//modules[index], -1, modules[index])

    return x

def allPairsAreCoprime(list):
    for index in range(0,len(list)-1):
        for secondIndex in range(index+1, len(list)):
            if gcd(list[index], list[secondIndex]) != 1:
                return False
    return True

def euclideanAlgorithm(a, b):
    #exit condition
    if a == 0:
        return b
    if b == 0:
        return a

    if a > b:
        a = a%b
    else:
        b= b%a

    #its recucrsive funciton
    euclideanAlgorithm(a,b)
