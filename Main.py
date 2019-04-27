import random
from math import sqrt
from random import randint

from Point import Point
from Curve import generate
from PointCalculator import addPoints, multiplyPoint, mul
from Utils import generatePrimeNumber, testEuler,isOnCurve
import Alice
import Bob

#ALICE

prime = Alice.generatePrime(254)
print("prime number: ", prime)
curve = Alice.generateElipticCurve(prime)
print("curve: ", curve)
print("is curve correct: ",curve.isCorrect())
point = Alice.generatePointOnE(curve)

print("Q: ", point)
print("is point on curve: ", isOnCurve(curve,point.x, point.y))
xA = Alice.generateX(prime)
print("xA: ", xA)
Pa = Alice.generatePa(curve, point, xA)
print("Pa: ", Pa)
print("is Pa on curve: ",isOnCurve(curve, Pa.x, Pa.y))

#BOB
xB = Bob.generateX(prime)
Pb = Bob.generatePb(curve, point, xB)

#ALICE
secretA = Alice.generateSecret(curve, xA, Pb)
secretB = Bob.generateSecret(curve, xB, Pa)
print("secret A: ", secretA)
print("secret B: ", secretB)
# print("generating prime number...")
# prime = generatePrimeNumber()
# print("prime number: ", prime)
# print("generating eliptic curve...")
# curve = generate(prime)
# print("Curve: ", curve)
# print("generating point...")
#
#
# correctPoint = False
# while (not correctPoint):
#     x = random.randrange(1,prime)
#     f = curve.calculate(x)
#     test = testEuler(f, prime, curve.modulo)
#     if(test):
#         p = (prime +1) / 4
#         y = pow(f, ((prime+1)//4), curve.modulo)
#         point = Point(x,y)
#         print("Point: x=",x ,", y=", y)
#         correctPoint = True
#
#         #tutaj mamy poprawny punkt i krzywą
#
#         # result = addPoints(curve, point, point)
#         # r2 = mul(curve, point, 83218327)
#         # isOnCurve(curve, r2.x, r2.y)
#         # print("result: ", r2)

