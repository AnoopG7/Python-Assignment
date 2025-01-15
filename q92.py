# Create classes Rectangle and Square. Square should inherit from Rectangle in a way that automatically sets length and width to the same value.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

rectangle = Rectangle(4, 5)
square = Square(4)
print("Rectangle area:", rectangle.area())
print("Square area:", square.area()) 