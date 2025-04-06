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
