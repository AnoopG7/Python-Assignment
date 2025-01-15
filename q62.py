# Create a base class Animal and a derived class Dog. Override a method speak() in the Dog class to print "Woof!".
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()