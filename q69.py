# Write a recursive function that computes the sum of all elements in a list.
def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recursive_sum(lst[1:])

print("Sum of list [1, 2, 3, 4]:", recursive_sum([1, 2, 3, 4]))