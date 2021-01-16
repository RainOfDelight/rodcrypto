a=66528
b=52920
ended = False
while not ended:
    if a > b:
        a = a%b
    elif b > a:
        b= b%a
    else:
        print("Non dovrei arrivare qui")
    if a == 0:
        print("GCD = ", b)
        ended = True
    if b == 0:
        print("GCD = ", a)
        ended = True