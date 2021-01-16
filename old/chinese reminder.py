
import math

#print(5*11*17)
def chineseReminder(congruences, modules):
    """
    x ≡ 2 mod 5
    x ≡ 3 mod 11
    x ≡ 5 mod 17
    Find the integer a such that x ≡ a mod 935
    [2,3,5] -> goes in the congruences array
    [5,11,17] -> goes in the modules array
    """
    assert (len(congruences) == len(modules)), 'The length of the 2 input arrays must be the same'
    assert allPairsAreCoprime(modules), 'The modules are not coprime. For the Chinese Reminder to work they must be coprime'

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
            if math.gcd(list[index], list[secondIndex]) != 1:
                return False
    return True
