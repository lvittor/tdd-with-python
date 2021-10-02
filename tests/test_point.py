import unittest

from src.Point import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        """
            Creates a Point() object with (x, y) = (3.0, 4.0)
        """
        self.point = Point(3.0, 4.0)

    def test_get_x(self):
        self.assertEqual(self.point.get_x(), 3.0)

    def test_get_y(self):
        self.assertEqual(self.point.get_y(), 4.0)

    def test_distanceTo(self):
        p2 = Point(0.0, 0.0)
        self.assertEqual(self.point.distanceTo(p2), 5.0)

    def test_equals(self):
        p2 = Point(3.0, 4.0)
        p3 = Point(1.2, 2.9)
        self.assertEqual(self.point, p2)
        self.assertNotEqual(self.point, p3)

    def test_str(self):
        self.assertEqual(self.point.__str__(), "Point [x:3.00, y:4.00]")
