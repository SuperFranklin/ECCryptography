from Point import Point


def addPoints(c, p1, p2):

    if p1.infinity:
        return p2

    if p2.infinity:
        return p1

    if p1.x != p2.x:
        m = ((p2.y - p1.y) * modinv((p2.x - p1.x), c.modulo)) % c.modulo
        x = (pow(m,2,c.modulo) - p1.x - p2.x) % c.modulo
        y = (m*(p1.x -x) - p1.y) % c.modulo
        return Point(x, y)

    if p1.x == p2.x and p1.y != p2.y:
        return Point.generateInfinity()

    if p1 == p2 and p1.y !=0:
        m = (((3*pow(p1.x, 2 , c.modulo)) + c.A) * modinv(2 * p1.y, c.modulo)) % c.modulo
        x = (pow(m, 2, c.modulo) - 2*p1.x) % c.modulo
        y = (m*(p1.x - x) - p1.y) % c.modulo
        return Point(x,y)

    if p1 == p2 and p1.y ==0:
        return Point.generateInfinity()

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1)

def modinv(a, m):
    g, x = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m