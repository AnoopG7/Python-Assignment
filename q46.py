# Count how often each element appears in a list and store the result in a dictionary.
lst = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 6, 6, 7]
frequency_dict = {x: lst.count(x) for x in set(lst)}
print("Frequency of elements:", frequency_dict)