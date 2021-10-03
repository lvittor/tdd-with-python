import pytest
import sys

from src.Circle import Circle 
from src.Point import Point

circles = [
    {"center": Point(0.0, 0.0), "radius": 2.3},
    {"center": Point(2.0, 1.0), "radius": 7.3},
]

@pytest.fixture(scope="module", params=circles)
def setup(request):
    circle = Circle(request.param["center"], request.param["radius"])
    yield circle

def test_area(setup):
    assert pytest.approx(setup.area(), 0.1) in [16.6, 167.4]

def test_perimeter(setup):
    assert pytest.approx(setup.perimeter(), 0.1) in [14.4, 45.8]

def test_str(setup):
    assert f"{setup}" in [
                            "Circle [Center: Point [x:0.00, y:0.00], Radius: 2.30]",
                            "Circle [Center: Point [x:2.00, y:1.00], Radius: 7.30]"
                         ]

def test_is(setup):
    assert isinstance(setup, Circle) 


@pytest.mark.skip(reason="This could be used to avoid a test")
def test_skip():
    pass

@pytest.mark.skipif(True, reason="This could also be used to avoid a test")
def test_skipif():
    pass