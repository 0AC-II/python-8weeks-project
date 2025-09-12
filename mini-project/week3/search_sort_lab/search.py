# search.py
def linear_search(arr, target):
    """Perform Linear Search"""
    for i, val in enumerate(arr):
        if val == target:
            return i # Return the index if found
    return -1 # Return -1 if not found


def binary_search(arr, target):
    """Perform Binary Search (assumes sorted list)"""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
