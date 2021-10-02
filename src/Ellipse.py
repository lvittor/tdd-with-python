from src.Figure import Figure
from src.Point import Point

from math import pi
from math import sqrt


class Ellipse(Figure):

    def __init__(self, centerPoint: Point, sMayorAxis: float, sMinorAxis: float):
        self.centerPoint = centerPoint
        self.sMayorAxis = sMayorAxis
        self.sMinorAxis = sMinorAxis

    def area(self) -> float:
        return pi * self.sMayorAxis * self.sMinorAxis

    def perimeter(self) -> float:
        return 2 * pi * sqrt((self.sMayorAxis ** 2 + self.sMinorAxis ** 2) / 2)

    def __str__(self):
        return f"Ellipse [Center: {self.centerPoint}, sMayorAxis: {self.sMayorAxis:.2f}, " \
               f"sMinorAxis: {self.sMinorAxis:.2f}]"
