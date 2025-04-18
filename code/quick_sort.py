import random
import time
from functools import wraps


def timer(func):
    """Decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper


def create_data(length):
    """Create a list of random integers."""
    data = [random.randint(1, 10000) for _ in range(length)]
    return data

@timer
def bubble_sort(arr):
    """
    Sort a list using the bubble sort algorithm.
    This implementation includes duplicates.
    """
    for i in arr:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

@timer
def bubble_sort_opt(arr):
    """
    Sort a list using the optimized bubble sort algorithm.
    This implementation includes duplicates.
    """
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to detect if any swaps are made
        for j in range(n - i - 1):  # Reduce the range with each pass
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps were made, the array is already sorted
            break
    return arr


def quick_sort(arr):
    """Sort a list using the quicksort algorithm, including duplicates."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  # Include duplicates
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_reduced_data(arr):
    """Sort a list using the quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


@timer
def call_quick_sort(arr):
    """Call quick_sort function."""
    return quick_sort(arr)


if __name__ == "__main__":
    data = create_data(10)
    print(f"Unsorted data: {data}")
    print("Sorting data...")
    # data = [1, 26, 6, 88, 16, 72, 8, 68, 56, 96, 55]
    print("Sorting data with base quicksort...")
    result = call_quick_sort(data)
    print(f"Sorted data with base quicksort: {result}")
    # result2 = bubble_sort(data)
    # print(f"Sorted data with bubble sort: {result2}")
    # result3 = bubble_sort_opt(data) 
    # print(f"Sorted data with optimized bubble sort: {result3}")
    # result2 = bubble_sort(data)