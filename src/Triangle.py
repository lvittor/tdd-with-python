from Figure import Figure
from Point import Point

class Triangle(Figure):
    def __init__(self, firstPoint: Point, secondPoint: Point, thirdPoint: Point):
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.thirdPoint = thirdPoint
    
    def area(self) -> float:
        semiPerimiter = self.perimeter() / 2
        return sqrt(semiPerimiter * (semiPerimiter - self.firstSide()) * (semiPerimiter - self.secondSide()) * (semiPerimiter - self.thirdSide()))
    
    def perimeter(self) -> float:
        return self.firstSide() + self.secondSide() + self.thirdSide()
    
    def firstSide(self) -> float:
        return self.firstPoint.distanceTo(self.secondPoint)
    
    def secondSide(self) -> float:
        return self.secondPoint.distanceTo(self.thirdPoint)

    def thirdSide(self) -> float:
        return self.thirdPoint.distanceTo(self.firstPoint)
    
    def __str__(self):
        return f"Triangle [{self.firstPoint}, {self.secondPoint}, {self.thirdPoint}]"