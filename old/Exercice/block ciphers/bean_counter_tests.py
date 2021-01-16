from Crypto.Cipher import AES
import os
#Questo file l'ho modificato per fare delel prove
KEY = b"00000000000000000000000000000000"


class StepUpCounter(object):
    def __init__(self, value=os.urandom(16), step_up=False):
        self.value = value.hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            self.newIV = hex(int(self.value, 16) - self.stup)   # Qui e' stato usato stup che e' sempre False!! Per questo il valore non cambia
        self.value = self.newIV[2:len(self.newIV)]                  #False e' come se fosse 0
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value



#@chal.route('/bean_counter/encrypt/')
def encrypt():
    cipher = AES.new(KEY, AES.MODE_ECB)
    ctr = StepUpCounter()

    out = []
    with open("bean_flag.png", 'rb') as f:
        block = f.read(16)
        while block:
            keystream = cipher.encrypt(ctr.increment())     #keystream is always the same
            xored = [a^b for a, b in zip(block, keystream)]
            out.append(bytes(xored).hex())
            block = f.read(16)

    return ''.join(out)

#print(encrypt())

with open("bean_flag.png", 'rb') as f:
    block = f.read(4)
    print(block)