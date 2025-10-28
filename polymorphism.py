# Polymorphism in Python
# This demonstrates method overriding and duck typing.

# Base class
class Shape:
    def area(self):
        pass  # Abstract method

# Derived classes
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphism: Same method name, different behavior
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")  # Outputs: Area: 20, then Area: 28.26