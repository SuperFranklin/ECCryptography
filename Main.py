import random
from random import randint

from Point import Point
from Curve import generate

#is prime test
def miller_rabin(n, k):
    if n == 2:
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

def generatePrimeNumber():
    isPrime = False
    while(not isPrime):
        k = random.getrandbits(254)
        p = ( 4*k )+ 3
        isPrime = miller_rabin(p,128)

    return p

def testEuler(y, p, modulo):
    fp = pow(y,((p-1)//2), modulo)
    if(fp == 1):
        return True
    print("y= ",y , "is not correct")
    return False

print("generating prime number...")
prime = generatePrimeNumber()
print("prime number: ", prime)
print("generating eliptic curve...")
curve = generate(prime)
print("Curve: ", curve)
print("generating point...")
correctPoint = False
while (not correctPoint):
    x = random.randrange(1,prime)
    f = curve.calculate(x)
    test = testEuler(f, prime, curve.modulo)
    if(test):
        p = (prime +1) / 4
        y = pow(f, ((prime+1)//4), curve.modulo)
        point = Point(x,y)
        print("Point: x=",x ,", y=", y)
        correctPoint = True