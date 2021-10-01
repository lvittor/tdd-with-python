import unittest

from src.Point import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point = Point(3.0, 4.0)

    def test_get_x(self):
        self.assertEqual(self.point.get_x(), 3.0)

    def test_get_y(self):
        self.assertEqual(self.point.get_y(), 4.0)

    def test_distanceTo(self):
        p2 = Point(0.0, 0.0)
        self.assertEqual(self.point.distanceTo(p2), 5.0)