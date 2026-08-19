# Implement the following class diagram:
# Polygon (abstract class)
     # - Number of sides (attributes)
     # - Perimeter (abstract method)
     # - Area (abstract method
""" Square (subclass)
        - length of one side (attributes)
        - perimeter (method)
        - area (method) """
""" Circle (subclass)
        - radius of the circle
        - perimeter (method)
        - area (method) """

from abc import ABC, abstractmethod
from math import pi


class Polygon(ABC):
    def __init__(self, sides_qtt: int):
        self.sides = sides_qtt

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Square(Polygon):
    def __init__(self, side_length: float):
        super().__init__(sides_qtt = 4)
        self.length = side_length

    def perimeter(self) -> float:
        return self.sides * self.length

    def area(self) -> float:
        return self.length ** 2


class Circle(Polygon):
    def __init__(self, radius: float):
        super().__init__(sides_qtt = 0)
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * pi * self.radius

    def area(self) -> float:
        return pi * self.radius ** 2

