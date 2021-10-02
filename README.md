# unittest — Unit testing framework

![](https://github.com/lvittor/tdd-with-python/actions/workflows/main.yml/badge.svg?branch=unittest)

> *"The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework."*
> - <cite>[Python docs](docs.python.org/3/library/unittest.html)</cite>

## Requirements
To run the tests you should first install the project requirements.
- python >=3.8
- poetry >= 1.1.1
- pip >= 21.0.1

If you do not have this installed, you can do so by running the following commands. 

```bash
sudo apt install python3 
sudo apt install pip
pip install poetry
poetry install
```

For Windows installation you can follow the [Python documentation](https://www.python.org/downloads/) and [Pip tutorial](https://www.liquidweb.com/kb/install-pip-windows/)

## Running the tests
With all the requirements met, you can, for lack of a better word, test the tests, by running the folowing command:

```bash
poetry run python -m unittest tests/test_suite.py
```

You should expect an output such as this one:

```bash
test_distanceTo (tests.test_point.TestPoint) ... ok
test_equals (tests.test_point.TestPoint) ... ok
test_get_x (tests.test_point.TestPoint) ... ok
test_get_y (tests.test_point.TestPoint) ... ok
test_str (tests.test_point.TestPoint) ... ok
test_area (tests.test_rectangle.TestRectangle) ... ok
test_base (tests.test_rectangle.TestRectangle) ... ok
test_even_area (tests.test_rectangle.TestRectangle) ... ok
test_height (tests.test_rectangle.TestRectangle) ... ok
test_is_rectangle (tests.test_rectangle.TestRectangle) ... ok
test_perimeter (tests.test_rectangle.TestRectangle) ... ok
test_str (tests.test_rectangle.TestRectangle) ... ok
test_area (tests.test_triangle.TestTriangle) ... ok
test_is (tests.test_triangle.TestTriangle) ... ok
test_perimeter (tests.test_triangle.TestTriangle) ... ok
test_str (tests.test_triangle.TestTriangle) ... ok
test_area (tests.test_ellipse.TestEllipse) ... ok
test_is (tests.test_ellipse.TestEllipse) ... ok
test_perimeter (tests.test_ellipse.TestEllipse) ... ok
test_str (tests.test_ellipse.TestEllipse) ... ok
testSkip (tests.test_circle.TestCircle) ... skipped 'This could be used to avoid a test'
test_area (tests.test_circle.TestCircle) ... Test finished!
ok
test_is (tests.test_circle.TestCircle) ... Test finished!
ok
test_perimeter (tests.test_circle.TestCircle) ... Test finished!
ok
test_perimeter_fail (tests.test_circle.TestCircle) ... Test finished!
expected failure
test_str (tests.test_circle.TestCircle) ... Test finished!
ok

----------------------------------------------------------------------
Ran 26 tests in 0.001s

OK (skipped=1, expected failures=1)
```

To run any particular test, you can execute the following command:

```bash
$>  poetry run python -m unittest <test>
```