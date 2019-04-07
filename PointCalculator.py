from Point import Point


def addPoints(c, p1, p2):
    if p1.x != p2.x:
        m = ((p2.y - p1.y) / (p2.x - p1.x)) % c.modulo
        x = (m**2 - p1.x - p2.x) % c.modulo
        y = (m*(p1.x -x) - p1.y) % c.modulo
        return Point(x, y)

    if p1.x == p2.x and p1.y != p2.y:
        return Point(8888,8888)

    if p1 == p2 and p1.y !=0:
        m = (((3*p1.x) + c.A) / 2 * p1.y) % c.modulo
        print(m)
        x = (m**2 - 2*p1.x) % c.modulo
        print(x)
        y = (m*(p1.x - x) / 2*p1.y) % c.modulo
        print(y)
        print("hello")
        return Point(x,y)
    if p1 == p2 and p1.y ==0:
        return Point(8888, 8888)