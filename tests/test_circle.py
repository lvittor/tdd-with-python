import unittest

from src.Circle import Circle 
from src.Point import Point


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(Point(0.0, 0.0), 2.3)
    
    def test_area(self):
        self.assertAlmostEqual(self.circle.area(), 16.61903, places=4)
    
    def test_perimeter(self):
        self.assertAlmostEqual(self.circle.perimeter(), 14.45133, places=4)

    @unittest.expectedFailure
    def test_perimeter_fail(self):
        self.assertAlmostEqual(self.circle.perimeter(), 14, places=4)
    
    def test_str(self):
        self.assertEqual(self.circle.__str__(), "Circle [Center: Point [x:0.00, y:0.00], Radius: 2.30]")

    def test_is(self):
        self.assertIsInstance(self.circle, Circle)

    def tearDown(self):
        print("Test finished!")

    """ 
    Decorators are a very useful tool to avoid a 
    test, skip it if a condition is met or isolate a test. 
    
    More info can be found in: https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures 
    """
    @unittest.skip("This could be used to avoid a test")
    def testSkip(self):
        self.fail("Oh no!")
