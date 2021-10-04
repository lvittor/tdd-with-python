import pytest

from src.Point import Point
from src.Rectangle import Rectangle

rectangles = [
    {"p1": Point(0, 0), "p2": Point(5, 5)},
    {"p1": Point(2, 3), "p2": Point(-5, 1)}
]


@pytest.fixture(scope="module", params=rectangles)
def setup(request):
    rectangle = Rectangle(request.param["p1"], request.param["p2"])
    yield rectangle


def test_area(setup):
    assert setup.area() in [25, 14]


def test_perimeter(setup):
    assert setup.perimeter() in [20, 18]


def test_str(setup):
    assert f"{setup}" in [
        "Rectangle [Point [x:0.00, y:0.00], Point [x:5.00, y:5.00]]",
        "Rectangle [Point [x:2.00, y:3.00], Point [x:-5.00, y:1.00]]"
    ]


def test_is(setup):
    assert isinstance(setup, Rectangle)
