import unittest
from Curve import generate, Curve
from Point import Point
from PointCalculator import addPoints, multiplyPoint

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
        assert r==correctResult, "incorrect result"


        #x1!=x2
    def test_addCaseFour(self):
        c = Curve(2,9,13)
        assert c.isCorrect(), "curve is not correct"
        p1 = Point(6,9)

        p2 = Point(4,2)
        r = addPoints(c, p1, p2)
        correctResult = Point(12,9)
        assert r==correctResult, "incorrect result"

    #simple numbers
    def test_multiply(self):
        c = Curve(2,9,13)
        p = Point(6,9)
        r = multiplyPoint(c, p, 4)
        correctResult = Point(1,8)
        assert r==correctResult, "incorrect result"

    #big numbers
    def test_multiply2(self):
        c = Curve(9,9,1220688155435260123416698775875983763836072035444529752273150378775402574239)
        p = Point(924812513218946557760338246264312520657414397880413636853317984556123176672,
                  901482186226661984437937203673347769982210913465995729381057735314565221292)
        r = multiplyPoint(c, p, 932)
        correctResult = Point(998036328406205595765169951306681464055471715091787640432371773378967290101,
                              1032505436168794803391453916475059567680570631100446822540746527697742553389)
        assert r==correctResult, "incorrect result"


if __name__ == '__main__':
    unittest.main()

