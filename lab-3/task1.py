import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, identifier, x, y):
        self.id = identifier
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    @abstractmethod
    def is_intersect(self, other):
        pass

    @abstractmethod
    def is_include(self, other):
        pass


class Pentagon(Shape):
    def __init__(self, identifier, x, y, radius):
        super().__init__(identifier, x, y)
        self.radius = radius

    def is_intersect(self, other):
        if isinstance(other, Pentagon):
            distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            return distance < (self.radius + other.radius)
        return False

    def is_include(self, other):
        if isinstance(other, Pentagon):
            distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            return distance + other.radius <= self.radius
        return False
