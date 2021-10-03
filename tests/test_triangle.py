import pytest

from src.Point import Point
from src.Triangle import Triangle

triangles = [
    {"p1": Point(1.0, 0.0), "p2": Point(5.0, 0.0), "p3": Point(3.0, 4.0)},
    {"p1": Point(0.0, 0.0), "p2": Point(2.0, 3.0), "p3": Point(3.0, 7.0)},
]

@pytest.fixture(scope="module", params=triangles)
def setup(request):
    triangle = Triangle(request.param["p1"], request.param["p2"], request.param["p3"])
    yield triangle

def test_area(setup):
    assert pytest.approx(setup.area(), 0.1) in [8, 2.5]

def test_perimeter(setup):
    assert pytest.approx(setup.perimeter(), 0.1) in [13, 15.3]

def test_str(setup):
    assert f"{setup}" in [
                            "Triangle [Point [x:1.00, y:0.00], Point [x:5.00, y:0.00], Point [x:3.00, y:4.00]]",
                            "Triangle [Point [x:0.00, y:0.00], Point [x:2.00, y:3.00], Point [x:3.00, y:7.00]]"
                         ]

def test_is(setup):
    assert isinstance(setup, Triangle)



