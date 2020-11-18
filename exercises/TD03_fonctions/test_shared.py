from random import randint as rand


class stop:
    def __init__(self, id):
        self.x = rand(1, 100)
        self.y = rand(1, 100)
        self.t = id


numClient = 0


class client:
    def __init__(self):
        numClient += 1
        self.o = stop(numClient)
        self.d = stop(numClient)


X = list()
Y = list()
num = 3


def add():
    best = 1000000
    c = random.choice(X)
    X.remove(c)
    for o in Y:
        Y.insert(Y.index(o), c.o)
        for d in Y:
            Y.insert(Y.index(d), c.d)
            if computelength() < best:
                best = computelength()
                bestO = o
                bestD = d
            Y.remove(c.d)
        Y.remove(c.o)
    Y.insert(Y.index(bestO), c.o)
    Y.insert(Y.index(bestD), c.d)


def remove():
    a = random.choice(Y)
    for s in Y:
        if s.id == a.id:
            Y.remove(s)


def computelength():
    total = 0
    prev = Y.front()
    for s in Y:
        total += distance(prev, s)
        prev = s


def solve:




    
for i in range(num):
    X.append(client())

