# Create a class that uses the @property decorator to get/set an attribute with validation logic.
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Temperature below -273.15 is not possible!")
        else:
            self._celsius = value

temp = Temperature(25)
print("Current temperature:", temp.celsius)
temp.celsius = -300
temp.celsius = 30
print("Updated temperature:", temp.celsius)