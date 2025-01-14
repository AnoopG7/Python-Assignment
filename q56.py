# Write a function that attempts to convert a string to an integer, catching any ValueError and printing a custom message.
def convert_to_int(value):
    try:
        result = int(value)
        print("Conversion successful! The integer value is:", result)
    except ValueError:
        print("Error: The provided string is not a valid integer.")

# Example usage
value = input("Enter a value to convert to an integer: ")
convert_to_int(value)
