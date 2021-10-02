import unittest

from src.Rectangle import Rectangle
from src.Point import Point

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(Point(0.0, 0.0), Point(1.0, 2.0))
    
    def test_base(self):
        self.assertAlmostEqual(self.rectangle.base(), 1)
    
    def test_height(self):
        self.assertAlmostEqual(self.rectangle.height(), 2)

    def test_area(self):
        self.assertAlmostEqual(self.rectangle.area(), 2)

    def test_perimeter(self):
        self.assertAlmostEqual(self.rectangle.perimeter(), 6)
    
    def test_str(self):
        self.assertEqual(self.rectangle.__str__(), "Rectangle [Point [x:0.00, y:0.00], Point [x:1.00, y:2.00]]")

    def test_is_rectangle(self):
        self.assertIsInstance(self.rectangle, Rectangle)