class Point:
    x = 0.0
    y = 0.0
    infinity = False

    def __init__(self, x=0.0, y=0.0, infiniy=False):
        self.x = x
        self.y = y
        self.infinity = infiniy


    def generateInfinity():
        p = Point()
        p.infinity = True
        return p



    def __str__(self):
        return "Point: ({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
