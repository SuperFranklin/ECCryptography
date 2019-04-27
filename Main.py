import random

from Point import Point
from Curve import generate
from PointCalculator import addPoints, multiplyPoint, mul
from Utils import generatePrimeNumber, testEuler,isOnCurve



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
        r2 = mul(curve, point, 83218327)
        isOnCurve(curve, r2.x, r2.y)
        print("result: ", r2)

