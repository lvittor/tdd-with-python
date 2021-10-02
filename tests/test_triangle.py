import unittest

from src.Triangle import Triangle
from src.Triangle import Point


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle(Point(1.0, 0.0), Point(5.0, 0.0), Point(3.0, 4.0))

    def test_area(self):
        self.assertAlmostEqual(self.triangle.area(), 8)

    def test_perimeter(self):
        self.assertAlmostEqual(self.triangle.perimeter(), 12.9442719)

    def test_str(self):
        self.assertEqual(self.triangle.__str__(),
                         "Triangle [Point [x:1.00, y:0.00], Point [x:5.00, y:0.00], Point [x:3.00, y:4.00]]")

    def test_is(self):
        self.assertIsInstance(self.triangle, Triangle)
