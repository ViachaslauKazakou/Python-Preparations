"""

Найти все числа, исчезнувшие в массиве

Условие:
Дан массив nums, в которой числа из диапазона [1, n]. Необходимо вывести числа из [1, n], которых нет в nums.

Пример 1:

Вход: nums = [4,3,2,7,8,2,3,1].
Выход: [5,6]
"""
from main import timer


@timer
def func1(nums):
    set1 = set(nums)
    set2 = set(i for i in range(1, len(nums) + 1))
    res = set2 - set1
    print(res)


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1, 13, 22, 12]
    func1(nums)
