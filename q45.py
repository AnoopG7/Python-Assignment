# Given a dictionary, invert it (keys become values, values become keys).
original_dict = {'a': 1, 'b': 2, 'c': 3}
print("Origional dictionary:", original_dict)
inverted_dict = {v: k for k, v in original_dict.items()}
print("Inverted dictionary:", inverted_dict)