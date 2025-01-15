# Create a class Counter with a class variable count. Implement a @classmethod to increment count and a @staticmethod to display a utility message.
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def utility_message():
        print("This is a static method with no access to class variables.")

Counter.increment()
Counter.increment()
print("Count:", Counter.count)
Counter.utility_message()