from math import sqrt

from PointCalculator import mul
from Utils import generatePrimeNumber, testEuler, isOnCurve
import random
from Curve import generate
from Point import Point


def generatePrime(numOfBits):
    return generatePrimeNumber(numOfBits)


def generateElipticCurve(prime):
    test = False
    curve = generate(prime)
    while not test:
        x = random.randrange(1, prime)
        f = curve.calculate(x)
        test = testEuler(f, prime, curve.modulo)
    return curve

def generatePointOnE(curve):
    prime = curve.modulo
    correctPoint = False
    while (not correctPoint):
        x = random.randrange(1,prime)
        f = curve.calculate(x)
        p = (prime +1) / 4
        y = pow(f, ((prime+1)//4), curve.modulo)
        point = Point(x,y)
        if(isOnCurve(curve,point.x, point.y)):
            return point

def generateX(prime):
    xLimit = prime +1 - 2* sqrt(prime)
    return random.randint(0, xLimit)

def generatePa(curve, point, x):
    return mul(curve, point, x)


def generateSecret(curve, xA, Pb):
    return mul(curve, Pb, xA)
