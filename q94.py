# Demonstrate polymorphism by defining a method draw() in multiple classes and calling draw() on a list of shapes.
class Circle:
    def draw(self):
        print("Drawing a Circle")

class Triangle:
    def draw(self):
        print("Drawing a Triangle")

shapes = [Circle(), Triangle()]
for shape in shapes:
    shape.draw()
