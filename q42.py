# Find the second largest element in a list of unique integers.
def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()
    
    if len(unique_lst) > 1:
        return unique_lst[-2]
    else:
        return None

lst = [10, 20, 30, 40, 50]
print("Second largest element:", second_largest(lst))
