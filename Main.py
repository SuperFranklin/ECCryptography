import random

from Point import Point
from Curve import generate
from PointCalculator import addPoints
from Utils import generatePrimeNumber, testEuler

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


        result = addPoints(curve, point, point)
        print("result: ", result)

