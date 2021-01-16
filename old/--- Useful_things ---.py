"""from Crypto.Util.number import inverse   #d = inverse(e, phi) --> d = e^(-1) MOD phi
To factorize you can use : Elliptic Curve Method (ECM) and the Self-Initializing Quadratic Sieve (SIQS).

import decimal

con decimal puoi fare sqrt di numeri grandissimi

a = Decimal(numeroGrandissimo).sqrt()

from decimal import *
getcontext().prec = 1400        -> precisione dei numeri

result = Decimal(pow(ct,1/3))       -> per fare radici diverse da quadrata


import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'path/to/the/folder/I/want/to/include')

"""