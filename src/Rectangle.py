from src.Point import Point
from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, topLeft: Point, bottomRight: Point):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def base(self) -> float:
        return abs(self.topLeft.get_x() - self.bottomRight.get_x())

    def height(self) -> float:
        return abs(self.topLeft.get_y() - self.bottomRight.get_y())

    def area(self) -> float:
        return self.base() * self.height()

    def perimeter(self) -> float:
        return (self.base() + self.height()) * 2

    def __str__(self):
        return f"Rectangle [{self.topLeft}, {self.bottomRight}]"
