# Demonstrate multiple inheritance with two parent classes providing different functionalities to a child class.
class Printer:
    def print_data(self, data):
        print(f"Printing: {data}")

class Scanner:
    def scan_document(self):
        return "Scanned Document Data"

class AllInOne(Printer, Scanner):
    pass

device = AllInOne()
device.print_data("Hello World!")
print(device.scan_document())