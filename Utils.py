from Point import Point
from Curve import generate, Curve
from PointCalculator import addPoints, modinv
import random


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
        p = ( 4*k ) + 3
        isPrime = miller_rabin(p,128)

    return p

def testEuler(y, p, modulo):
    fp = pow(y,((p-1)//2), modulo)
    if(fp == 1):
        return True
    print("y= ",y , "is not correct")
    return False


def isOnCurve(curve, x, y):
    L = pow(y, 2, curve.modulo) % curve.modulo
    P = ((pow(x, 3, curve.modulo) % curve.modulo) + ((curve.A * x) % curve.modulo)) + (
            curve.B % curve.modulo) % curve.modulo
    print("L: ",L % curve.modulo)
    print("P: ",P % curve.modulo)
    if(L % curve.modulo == P % curve.modulo):
        return True
    return False
