import pytest

from src.Point import Point
from src.Ellipse import Ellipse

ellipses = [
    {"center": Point(0, 0), "sMayorAxis": 4, "sMinorAxis": 2},
    {"center": Point(3, -1), "sMayorAxis": 5, "sMinorAxis": 1}
]


@pytest.fixture(scope="module", params=ellipses)
def setup(request):
    ellipse = Ellipse(request.param["center"], request.param["sMayorAxis"], request.param["sMinorAxis"])
    yield ellipse


def test_area(setup):
    assert pytest.approx(setup.area(), 0.1) in [25.1, 15.7]


def test_perimeter(setup):
    assert pytest.approx(setup.perimeter(), 0.1) in [19.8, 22.6]


def test_str(setup):
    assert f"{setup}" in [
        "Ellipse [Center: Point [x:0.00, y:0.00], sMayorAxis: 4.00, sMinorAxis: 2.00]",
        "Ellipse [Center: Point [x:3.00, y:-1.00], sMayorAxis: 5.00, sMinorAxis: 1.00]"
    ]


def test_is(setup):
    assert isinstance(setup, Ellipse)
