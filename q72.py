# Write a recursive function that returns the number of vowels in a string.
def count_vowels_recursive(s):
    vowels = 'aeiouAEIOU'
    if not s:
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels_recursive(s[1:])

# Example usage
text = "Hello, world!"
print("Number of vowels:", count_vowels_recursive(text))
