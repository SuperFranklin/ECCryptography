from random import randint
class Curve:
    A = 0
    B = 0
    modulo = 13

    def __init__(self, A, B, modulo):
        self.A = A
        self.B = B
        self.modulo = modulo

    def isCorrect(self):
        delta = (4*(self.A**3)) + (27*(self.B**2))
        if delta % self.modulo == 0:
            return False
        return True

    def calculate(self, x):
        return pow(x, 3, self.modulo) + (self.A * x) + self.B

    def __str__(self):
        return "y^2 = x^3 + {}x + {}   modulo={}".format(self.A, self.B, self.modulo)


def generate(p):
    isCorrect = False
    a = 0
    b = 0
    while(not isCorrect):
        a = randint(1,10)
        b = randint(1,10)
        delta = (4*(a**3)) + (27*(b**2))
        print("delta= ", delta)
        if (delta % p !=0):
            print("Correct curve found")
            isCorrect = True
        else:
            print("Incorrect curve")
    return Curve(a,b,p)

