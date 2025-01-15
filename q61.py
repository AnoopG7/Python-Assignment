# Create a class Person with attributes name and age. Include a method greet() that prints "Hello, my name is <name>."
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

person = Person("Anoop", 18)
person.greet()
