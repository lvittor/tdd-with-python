# pytest - helps you write better programs

![Pytest](https://github.com/lvittor/tdd-with-python/actions/workflows/pytest.yml/badge.svg?branch=pytest)

> *"The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries."*
> - <cite>[Pytest docs](docs.pytest.org/en/6.2.x)</cite>

## Requirements
To run the tests you should first install the project requirements.
- <a href="https://www.python.org/">python >= 3.8</a>
- <a href="https://python-poetry.org/">poetry >= 1.1.1</a>
- <a href="https://pypi.org/project/pip/">pip >= 21.0.1</a>
- <a href="https://docs.pytest.org/en/6.2.x/">pytest >= 5.4.3</a> (The `poetry install` command handles this requirement)

If you do not have this installed, you can do so by running the following commands. 

```bash
sudo apt install python3 
sudo apt install pip
pip install poetry
poetry install
```

For Windows installation you can follow the [Python documentation](https://www.python.org/downloads/) and [Pip tutorial](https://www.liquidweb.com/kb/install-pip-windows/)

## Running the tests

With all the requirements met, you can, for lack of a better word, test the tests, by running the following command:

```bash
poetry run pytest -v
```

> The **-v** flag sets the output to be verbose, this can be ignored.


You should expect an output like this one:

```bash
================================= test session starts ==================================
platform linux -- Python 3.8.10, pytest-5.4.3, py-1.10.0, pluggy-0.13.1 -- /home/jerobrave/Desktop/ITBA/2021 2Q/INGSOFT/testing-in-python/env/bin/python
cachedir: .pytest_cache
rootdir: /home/jerobrave/Desktop/ITBA/2021 2Q/INGSOFT/testing-in-python
collected 44 items                                                                     

tests/test_circle.py::test_area[setup0] PASSED                                   [  2%]
tests/test_circle.py::test_perimeter[setup0] PASSED                              [  4%]
tests/test_circle.py::test_str[setup0] PASSED                                    [  6%]
tests/test_circle.py::test_is[setup0] PASSED                                     [  9%]
tests/test_circle.py::test_area[setup1] PASSED                                   [ 11%]
tests/test_circle.py::test_perimeter[setup1] PASSED                              [ 13%]
tests/test_circle.py::test_str[setup1] PASSED                                    [ 15%]
tests/test_circle.py::test_is[setup1] PASSED                                     [ 18%]
tests/test_circle.py::test_skip SKIPPED                                          [ 20%]
tests/test_circle.py::test_skipif SKIPPED                                        [ 22%]
tests/test_ellipse.py::test_area[setup0] PASSED                                  [ 25%]
tests/test_ellipse.py::test_perimeter[setup0] PASSED                             [ 27%]
tests/test_ellipse.py::test_str[setup0] PASSED                                   [ 29%]
tests/test_ellipse.py::test_is[setup0] PASSED                                    [ 31%]
tests/test_ellipse.py::test_area[setup1] PASSED                                  [ 34%]
tests/test_ellipse.py::test_perimeter[setup1] PASSED                             [ 36%]
tests/test_ellipse.py::test_str[setup1] PASSED                                   [ 38%]
tests/test_ellipse.py::test_is[setup1] PASSED                                    [ 40%]
tests/test_point.py::test_get_x[setup0] PASSED                                   [ 43%]
tests/test_point.py::test_get_y[setup0] PASSED                                   [ 45%]
tests/test_point.py::test_distanceTo[setup0] PASSED                              [ 47%]
tests/test_point.py::test_equals[setup0] PASSED                                  [ 50%]
tests/test_point.py::test_get_x[setup1] PASSED                                   [ 52%]
tests/test_point.py::test_get_y[setup1] PASSED                                   [ 54%]
tests/test_point.py::test_distanceTo[setup1] PASSED                              [ 56%]
tests/test_point.py::test_equals[setup1] PASSED                                  [ 59%]
tests/test_point.py::test_str PASSED                                             [ 61%]
tests/test_point.py::test_is PASSED                                              [ 63%]
tests/test_rectanagle.py::test_area[setup0] PASSED                               [ 65%]
tests/test_rectanagle.py::test_perimeter[setup0] PASSED                          [ 68%]
tests/test_rectanagle.py::test_str[setup0] PASSED                                [ 70%]
tests/test_rectanagle.py::test_is[setup0] PASSED                                 [ 72%]
tests/test_rectanagle.py::test_area[setup1] PASSED                               [ 75%]
tests/test_rectanagle.py::test_perimeter[setup1] PASSED                          [ 77%]
tests/test_rectanagle.py::test_str[setup1] PASSED                                [ 79%]
tests/test_rectanagle.py::test_is[setup1] PASSED                                 [ 81%]
tests/test_triangle.py::test_area[setup0] PASSED                                 [ 84%]
tests/test_triangle.py::test_perimeter[setup0] PASSED                            [ 86%]
tests/test_triangle.py::test_str[setup0] PASSED                                  [ 88%]
tests/test_triangle.py::test_is[setup0] PASSED                                   [ 90%]
tests/test_triangle.py::test_area[setup1] PASSED                                 [ 93%]
tests/test_triangle.py::test_perimeter[setup1] PASSED                            [ 95%]
tests/test_triangle.py::test_str[setup1] PASSED                                  [ 97%]
tests/test_triangle.py::test_is[setup1] PASSED                                   [100%]

============================ 42 passed, 2 skipped in 0.13s =============================
```
