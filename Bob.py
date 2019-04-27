import random
from math import sqrt

from PointCalculator import mul



def generateX(prime):
    xLimit = prime +1 - 2* sqrt(prime)
    return random.randint(0, xLimit)

def generatePb(curve, point, xB):
    return mul(curve, point, xB)

def generateSecret(curve, xB, Pa):
    return mul(curve, Pa, xB)
