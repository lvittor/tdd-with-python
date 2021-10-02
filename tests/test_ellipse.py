import unittest

from src.Ellipse import Ellipse 
from src.Point import Point


class TestEllipse(unittest.TestCase):

    def setUp(self):
        self.ellipse = Ellipse(Point(0.0, 0.0), 5.0, 2.0)
    
    def test_area(self):
        self.assertAlmostEqual(self.ellipse.area(), 31.4159265)
    
    def test_perimeter(self):
        self.assertAlmostEqual(self.ellipse.perimeter(), 23.92565684391282)
    
    def test_str(self):
        self.assertEqual(self.ellipse.__str__(), "Ellipse [Center: Point [x:0.00, y:0.00], sMayorAxis: 5.00, sMinorAxis: 2.00]")

    def test_is(self):
        self.assertIsInstance(self.ellipse, Ellipse)