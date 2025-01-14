# Write a function that returns the length of a string without using the built-in len().
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
x=input("Enter a string ")
print("Length of the string is :", string_length(x))