# Write a program that checks if a given string is a palindrome.
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
