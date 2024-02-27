def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Элемент не найден

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)
print("Индекс элемента:", result)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Элемент не найден

arr = [10, 5, 8, 1, 7, 3, 9, 6, 2, 4]
target = 7
result = linear_search(arr, target)
print("Индекс элемента:", result)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [10, 5, 8, 1, 7, 3, 9, 6, 2, 4]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [10, 5, 8, 1, 7, 3, 9, 6, 2, 4]
bubble_sort(arr)
print("Отсортированный массив:", arr)


def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    else:
        half = power(x, n // 2)
        return x * half * half

x = 2
n = 10
result = power(x, n)
print(f"{x} в степени {n} = {result}")
