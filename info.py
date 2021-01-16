#Block Cypthers
#--------------
#Shor's algorithm is a polynomial-time quantum computer algorithm for integer factorization.
#Grover's algorithm is a quantum algorithm that finds with high probability the unique input to a black box function that produces a particular output value, using just O ( N ) {\displaystyle O({\sqrt {N}})} O({\sqrt {N}}) evaluations of the function, where N {\displaystyle N} N is the size of the function's domain. It was devised by Lov Grover in 1996.
#It turns out that there is an attack(Biclique Attack) on AES that's better than bruteforce, but only slightly – it lowers the security level of AES-128 down to 126.1 bits, and hasn't been improved on for over 8 years.
#Finally, while quantum computers have the potential to completely break popular public-key cryptosystems like RSA via Shor's algorithm, they are thought to only cut in half the security level of symmetric cryptosystems via Grover's algorithm. (cut in half cause of the square root of N)


#generating e,d
from Crypto.Util.number import  inverse
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = p*q
phi =(p-1)*(q-1)
d = inverse(e,phi)

#encrypting a message
import hashlib
from Crypto.Util.number import bytes_to_long, long_to_bytes
N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689
flag = b"crypto{Immut4ble_m3ssag1ng}"
hashed_flag = hashlib.sha256(flag).hexdigest()  #gives a string
hashed_flag_bytes = bytes.fromhex(hashed_flag)  #gives a bytes
long = bytes_to_long(hashed_flag_bytes) #gives a long
encripted = pow(long,d,N)
bytesAgain = long_to_bytes(encripted) #those are bytes  here you will see \xc9\xbbj\xbb
hexx=bytesAgain.hex()   #this is a string               here you will see 'c9bb6abb' , note that in the bytes you saw j, and ere you see 6a, beaseuse if a byte is a ascii character you will see it as char in a bytes arry, here not, but they are the same

#encrypted and decrypting  the mesage
encripted = pow(long,e,N)
decrypted = pow(encripted, d, N) # I get


# to calculate the inverse of a number in modular arithmetic you have just to do

pow(number, -1, modulus)