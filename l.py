import math

class Shape:
    def get_area(self):
        pass

class Dimensions:
    def set_height(self,height):
        raise NotImplementedError("Subclasses must implement set_height")
    def set_width(self,width):
        raise NotImplementedError("Subclasses must implement set_width")
        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape,Dimensions):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def get_area(self,widht):
        return (self.width * self.height) / 2

class Rectangle(Shape,Dimensions):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.length * self.width

def set_width(Shape, width):
    if isinstance(Shape, Dimensions):
        Shape.set_width = width
    else:
        print("This shape doesn't use width")

def set_height(Shape, height):
    if isinstance(Shape, Dimensions):
        Shape.set_height = height
    else:
        print("This shape doesn't use height")

rectangle = Rectangle(45,53)
circle = Circle(35)
set_height(rectangle,35) #Set height of rectangle to 35
set_height(circle,35) #prints outs error