"""
In RSA the private key is the modular multiplicative inverse of the exponent e modulo the totient of N.
Given the two primes:
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
and the exponent:
e = 65537
What is the private key d?
"""

import EEA
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = p*q
phi =(p-1)*(q-1)

d = inverse(e,phi)

messaggio = b'Ciao dandon'
print("Messaggio Originale - > ", messaggio)
# To encrypt  amessage you do
messaggio_numeri = bytes_to_long(messaggio)
print("Messaggio in numeri - > ", messaggio_numeri)
cifrato = pow(messaggio_numeri,e,N)
cifrato2 = pow(messaggio_numeri,d,N)
print("Messaggio Cifrato - > ", cifrato)
print("Messaggio Cifrato 2 - > ", cifrato2)
print("Leggo messaggio cifrato - > ",long_to_bytes(cifrato))
decifrato = pow(cifrato, d, N)
decifrato2 = pow(cifrato2, e, N)
print("Messaggio Decifrato - > ", decifrato)
print("Leggo messaggio cifrato - > ",long_to_bytes(decifrato))
print("Leggo messaggio cifrato 2- > ",long_to_bytes(decifrato2))


"""
c = 77578995801157823671636298847186723593814843845525223303932
decrypted = pow(c,d,N)

print(decrypted)
"""