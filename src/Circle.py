from Ellipse import Ellipse
from Point import Point

class Circle(Ellipse):
    def __init__(centerPoint: Point, radius: float):
        super().__init__(centerPoint, 2 * radius, 2 * radius)

    def __str__(self):
        return f"Circle [Center: {self.centerPoint} , Radius: {self.sMayorAxis / 2:.2f}]"