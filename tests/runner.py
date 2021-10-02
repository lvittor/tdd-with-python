from tests import test_point
from tests import test_ellipse
from tests import test_circle
from tests import test_triangle
from tests import test_rectangle

import unittest


def suite():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromModule(test_point))
    test_suite.addTests(loader.loadTestsFromModule(test_rectangle))
    test_suite.addTests(loader.loadTestsFromModule(test_triangle))
    test_suite.addTests(loader.loadTestsFromModule(test_ellipse))
    test_suite.addTests(loader.loadTestsFromModule(test_circle))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
