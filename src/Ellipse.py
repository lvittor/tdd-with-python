from Figure import Figure
from Point import Point

from math import pi as PI

class Ellipse(Figure):

    def __init__(centerPoint: Point, sMayorAxis: float, sMinorAxis: float):
        self.centerPoint = centerPoint
        self.sMayorAxis = sMayorAxis
        self.sMinorAxis = sMinorAxis

    def area(self) -> float:
        return PI / 4 * self.sMayorAxis * self.sMinorAxis

    def perimeter(self) -> float:
        return PI / 2 * (self.sMayorAxis + self.sMinorAxis)

    def __str__(self):
        return f"Ellipse [Center: {self.centerPoint}, sMayorAxis: {self.sMayorAxis:.2f}, sMinorAxis: {self.sMinorAxis:.2f}]"