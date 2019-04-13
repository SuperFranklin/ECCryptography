import unittest
from Curve import generate, Curve
from Point import Point
from PointCalculator import addPoints

class  PointCalculatorTest(unittest.TestCase):

    #p1=p2 and p1.x != 0
    def test_addCaseOne(self):
        c = Curve(9,5,13)
        assert c.isCorrect(), "curve is not correct"
        p = Point(4,1)
        r = addPoints(c, p, p)
        correctResult = Point(8,2)
        assert r==correctResult, "should be (8,2)"

    #p1=p2 and p1.x != 0
    def test_addCaseOne2(self):
        c = Curve(2,2,47218595856952157806696569632545678027423892273209310176067431692817752992683)
        assert c.isCorrect(), "curve is not correct"
        p = Point(12862157267214899810361926955908539612877409450391118811465627945348641414699,
                  12019096858601327682205759357597394733984175977637230947682741345278170525625)
        r = addPoints(c, p, p)
        correctResult = Point(8427593452907253031911973389814307956594156143196768939002634990187043644156,
                              19381585424404293305376546768509776437754879171682733989060920467515335940764)
        assert r==correctResult, "incorect result"

    #x1=x2 and y1!=y2
    def test_addCaseTwo(self):
        c = Curve(2,2,13)
        assert c.isCorrect(), "curve is not correct"
        p1 = Point(4,3)

        p2 = Point(4,2)
        r = addPoints(c, p1, p2)
        correctResult = Point.generateInfinity()
        assert r==correctResult, "incorect result"

    #x1=x2 and y1=0
    def test_addCaseThree(self):
        c = Curve(2,2,13)
        assert c.isCorrect(), "curve is not correct"
        p1 = Point(4,0)

        p2 = Point(4,0)
        r = addPoints(c, p1, p2)
        correctResult = Point.generateInfinity()
        assert r==correctResult, "incorect result"

        #x1!=x2
    def test_addCaseFour(self):
        c = Curve(2,9,13)
        assert c.isCorrect(), "curve is not correct"
        p1 = Point(6,9)

        p2 = Point(4,2)
        r = addPoints(c, p1, p2)
        correctResult = Point(12,9)
        assert r==correctResult, "incorect result"



if __name__ == '__main__':
    unittest.main()

