import time
from functools import wraps
from decimal import Decimal


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end - start}")
        return result

    return wrapper


def factorial(nums):
    if nums == 1:
        return nums
    return nums * factorial(nums - 1)


@timer
def calc_zero(num):
    counter = 0
    str_num = str(num)
    print(f"{str_num}, len(str_num) = {len(str_num)}")
    for i in range(1, len(str_num) + 1):
        # print(f" {i}  - ({str_num[-i]})")
        if int(str_num[-i]) == 0:
            counter += 1
        else:
            return counter
    return counter


@timer
def calc_zero2(num):
    counter = 0
    print(num)
    while num % 10 == 0:
        counter += 1
        num = int(Decimal(num) / 10)
        print(num)
    return counter


def timeit():
    start = time.time()
    result = factorial()
    end = time.time()


if __name__ == "__main__":
    fc = factorial(35)
    print(calc_zero(fc))
    print("=" * 100)
    print(calc_zero2(fc))
