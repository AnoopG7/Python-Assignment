# Create a base class Animal and a derived class Dog. The Dog class should inherit attributes and methods from Animal.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make a sound."

class Dog(Animal):
    def speak(self):
        return "Woof!"

animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.name, "says:", animal.speak())
print(dog.name, "says:", dog.speak())