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


class Rectangle(Shape):
    def __init__(self, identifier, x, y, width, height):
        super().__init__(identifier, x, y)
        self.width = width
        self.height = height

    def is_intersect(self, other):
        if isinstance(other, Rectangle):
            return not (self.x + self.width < other.x or
                        self.x > other.x + other.width or
                        self.y + self.height < other.y or
                        self.y > other.y + other.height)
        return False

    def is_include(self, other):
        if isinstance(other, Rectangle):
            return (self.x <= other.x and
                    self.y <= other.y and
                    self.x + self.width >= other.x + other.width and
                    self.y + self.height >= other.y + other.height)
        return False
