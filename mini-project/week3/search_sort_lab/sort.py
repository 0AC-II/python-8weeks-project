# sort.py
def bubble_sort(arr):
    """Bubble Sort Algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]: # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap
    return arr


def quick_sort(arr):
    """Quick Sort Algorithm (recursive)"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively apply quick_sort to left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)