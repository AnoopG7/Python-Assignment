# Write a recursive function that takes a list which may contain nested lists and returns a flat list.
def flatten_recursive(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_recursive(item))
        else:
            flat_list.append(item)
    return flat_list

# Example usage
nested_list = [1, [2, [3, 4]], 5]
print("Flattened list:", flatten_recursive(nested_list))
