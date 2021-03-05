class LXFIQNN():
    def __init__(self, init, mask, length):
        self.init = init
        self.mask = mask
        self.lengthmask = 2**(length+1)-1

    def next(self):
        nextdata = (self.init << 1) & self.lengthmask 
        i = self.init & self.mask & self.lengthmask 
        output = 0
        while i != 0:
            output ^= (i & 1)
            i = i >> 1
        nextdata ^= output
        self.init = nextdata
        return output

    def random(self, nbit):
        output = 0
        for _ in range(nbit):
            output <<= 1
            output |= self.next()
        return output


from secret import init, FLAG
"""secret.py
import os
init = int.from_bytes(os.urandom(5), 'big')
FLAG = 'hgame{xxx}'
"""


prng = LXFIQNN(init, 0b1011001010001010000100001000111011110101, 40)

score = 0
for r in range(100):
    print(f"round {r} :: score {score}")
    try:
        guess = int(input("guess: "))
    except:
        break
    secret = prng.random(4)
    if secret == guess:
        print("Right")
        score += 1
    else:
        print(f"Wrong, the secret is {secret}")

if score >= 80:
    print(FLAG)