from decorators.main import timer
import random



@timer
def binary_search(arr, target):
    """ search in sorted array"""
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


def create_data(lenght=100, val=100):
    return [random.randint(0, val) for item in range(lenght)]


if __name__ == "__main__":

    lenght = 10
    arr = create_data(lenght=lenght)
    arr = [92, 83, 24, 87, 36, 84, 79, 88, 22, 79]
    print(arr)
    index = random.randint(0, lenght-1)
    print(f"index elem: {index}")
    target = arr[index]
    target = 92
    print(target)
    result = binary_search(arr, target)
    print("Индекс элемента:", result)