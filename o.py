from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def get_area(self):
        return self.length * 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

#you don't have to modify ShapeFactory class to add another shape
class ShapeFactory:
    def createShape(shape):
        return shape.get_area()