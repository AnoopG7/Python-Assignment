# Define classes Circle, Square, and Triangle each with a draw() method. Call draw() on a list of shape objects to demonstrate polymorphism.
class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

class Triangle:
    def draw(self):
        print("Drawing a triangle")

shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()