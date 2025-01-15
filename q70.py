# Implement binary search recursively to find an element in a sorted list.
def binary_search_recursive(lst, target, low, high):
    if low > high:
        return -1 
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search_recursive(lst, target, low, mid - 1)
    else:
        return binary_search_recursive(lst, target, mid + 1, high)

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
print("Element found at index:" if result != -1 else "Element not found.", result)
