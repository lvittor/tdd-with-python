from src.Point import Point

from tests import test_point
from tests import test_ellipse
from tests import test_circle
from tests import test_triangle
from tests import test_rectangle

import unittest

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(test_point))
    suite.addTests(loader.loadTestsFromModule(test_rectangle))
    suite.addTests(loader.loadTestsFromModule(test_triangle))
    suite.addTests(loader.loadTestsFromModule(test_ellipse))
    suite.addTests(loader.loadTestsFromModule(test_circle))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())