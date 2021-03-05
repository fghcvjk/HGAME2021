import os

flag = "xxxx"

class Cxx1ff:
    c4ff1x = int.from_bytes(os.urandom(8),'big')
    c66f6 = int.from_bytes(os.urandom(8),'big')
    c4ff10 = int.from_bytes(os.urandom(8),'big')
    def __init__(self, seed):
        self.state = seed

    def next(self):
        self.state = (self.state * self.c4ff1x + self.c66f6) % self.c4ff10
        return self.state

class Cxx2ff:
    c4ff1x = int.from_bytes(os.urandom(8),'big')
    c66f6 = int.from_bytes(os.urandom(8),'big')
    c4ff10 = int.from_bytes(os.urandom(8),'big')
    def __init__(self, seed):
        self.state = seed

    def next(self):
        self.state = (self.state * self.c4ff1x + self.c66f6) % self.c4ff10
        return self.state

class Cxx3ff:
    c4ff1x = int.from_bytes(os.urandom(8),'big')
    c66f6 = int.from_bytes(os.urandom(8),'big')
    c4ff10 = int.from_bytes(os.urandom(8),'big')
    def __init__(self, seed):
        self.state = seed

    def next(self):
        self.state = (self.state * self.c4ff1x + self.c66f6) % self.c4ff10
        return self.state


def test1():
    gen = Cxx1ff(123) 
    print((Cxx1ff.c4ff1x,Cxx1ff.c4ff10))
    print(gen.next())
    print(gen.next())
    t1 = input()
    try:
        if int(t1.strip())==Cxx1ff.c66f6:
            return 1
    except:
        pass
    return 0
    


def test2():
    gen = Cxx2ff(123)
    print((Cxx2ff.c4ff10))
    print(gen.next())
    print(gen.next())
    print(gen.next())
    t1 = input()
    t2 = input()
    try:
        if (int(t1.strip())==Cxx2ff.c4ff1x) and (int(t2.strip())==Cxx2ff.c66f6):
            return 1
    except:
        pass
    return 0

def test3():
    gen = Cxx3ff(123)
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())
    t1 = input()
    try:
        if int(t1.strip())==Cxx3ff.c4ff10:
            return 1
    except:
        pass
    return 0

if __name__ == "__main__":
    ans = 0
    ans += test1()
    ans += test2()
    ans += test3()
    if ans>=3:
        print("win")
        print(flag)
    else:
        print("fail")