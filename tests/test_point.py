import pytest

from src.Point import Point

points = [
    {"x": 3.0, "y": 4.0},
    {"x": 1.0, "y": 2.0},
]


@pytest.fixture(scope="module", params=points)
def setup(request):
    point = Point(request.param["x"], request.param["y"])
    yield point
    # tearDown the point


@pytest.fixture(scope="module")
def set_origin(request):
    return Point(0, 0)


def test_get_x(setup):
    assert setup.get_x() in [3.0, 1.0]


def test_get_y(setup):
    assert setup.get_y() in [4.0, 2.0]


def test_distanceTo(setup, set_origin):
    assert pytest.approx(setup.distanceTo(set_origin), 1.0) in [5, 2.23]


def test_equals(setup, set_origin):
    assert set_origin != setup
    assert setup in [Point(_["x"], _["y"]) for _ in points]


def test_str():
    pass


def test_is():
    pass
