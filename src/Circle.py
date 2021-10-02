from src.Ellipse import Ellipse
from src.Point import Point

class Circle(Ellipse):
    def __init__(self, centerPoint: Point, radius: float):
        super().__init__(centerPoint, radius, radius)

    def __str__(self):
        return f"Circle [Center: {self.centerPoint}, Radius: {self.sMayorAxis:.2f}]"