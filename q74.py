# Write a recursive function that checks if a string is a palindrome.
def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

# Example usage
string = "madam"
print("Is palindrome:", is_palindrome_recursive(string))
