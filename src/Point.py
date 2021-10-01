from math import sqrt

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_x(self) -> float:
        return self.x
    
    def get_y(self) -> float:
        return self.y

    def distanceTo(self, other) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"Point [x:{self.x:.2f}, y:{self.y:.2f}]"