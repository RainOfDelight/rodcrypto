import random

def primality_test_miller_rabin(n, k):
    # n is the number
    # k are the iterations
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def primality_test_fermat(n, k):
    # Implementation uses the Fermat Primality Test
    # If number is even, it's a composite number
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, n - 1)

        if pow(a, n - 1) % n != 1:
            return False
    return True

def primality_test_solovay_strassen(n, k=10):
     def jacobi(a, n):
         j = 1  # j is jacobi symbol
         while (a != 0):

             while (a % 2 == 0):  # loop till a is even number
                 j = j * pow(-1,
                             (n * n - 1) / 8)  # if n=3(mod 8) or n=5(mod 8) or simply (-1)^((n^2-1)/2)==-1 then j = -j
                 a = a / 2

             if not ((a - 3) % 4 or (
                     n - 3) % 4):  # if a=3(mod 4) and n=3(mod 4) [So, (a-3)%4 and (n-3)%4 = 0] or simply (-1)^((n 1)/2)==-1 then j = -j
                 j = -j

             a, n = n, a  # interchange(a,n)
             a = a % n
         return j
     if n == 2 or n == 3:
         return True
     if not n & 1:
         return False

     for i in range(k):
         a = random.randrange(2, n - 1)       # choose any random number from 1 to (n-1)
         x = jacobi(a, n)                     # find n's jacobi number

         y = pow(a, (n - 1) // 2, n)           # calculate legendre symbol from euler criterion formula , used // to get the int and not the float
         if y != 1 and y != 0:
             y = -1

         if (x == 0) or (y != x):             # if jecobi and eular criterion formula are not same (y != x) then the number is not prime
             return False
     return True

def primality_test_aks(p, useless):
    def expand_x_1(n):
        # This version uses a generator and thus less computations
        c = 1
        for i in range(n // 2 + 1):
            c = c * (n - i) // (i + 1)
            yield c

    if p == 2:
        return True

    for i in expand_x_1(p):
        if i % p:
            # we stop without computing all possible solutions
            return False
    return True


def test():
    tests = ['primality_test_miller_rabin', 'primality_test_fermat', 'primality_test_solovay_strassen',
             'primality_test_aks']
    for i in range(1,10000):
        num = random.randrange(2, 10000)
        print(num)
        ans=[0,0,0,0]
        for i in range(0, len(tests)):
            ans[i] = eval(tests[i] + "("+str(num)+",40)")
        assert(ans[0]==ans[1] and ans[1]==ans[2] and ans[2]==ans[3])