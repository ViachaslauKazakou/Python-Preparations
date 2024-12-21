from pprint import pprint
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.8f} seconds")
        return result
    return wrapper

@timeit
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def seat1(a, b):
    # create array
    # arr = [[0 for i in range(a)] for j in range(b)]
    arr = [[0]*a for j in range(b)]
    student_number = 1
    for j in range(b):
        for i in range(a):
            arr[j][i] = student_number
            student_number += 1

    return arr    


def seat2(a, b):
    # create array
    student_number = 1
    arr = [[0]*a for j in range(b)]
    for j in range(a):
        for i in range(b):
            arr[i][j] = student_number
            student_number += 1
    return arr


@timeit
def count_students_in_same_seat(a, b):
    arr1 = seat1(a, b)
    arr2 = seat2(a, b)
    
    same_seat_count = 0
    for i in range(b):
        for j in range(a):
            if arr1[i][j] == arr2[i][j]:
                same_seat_count += 1
    
    return same_seat_count

# n, m = map(int, input("enter params(a,b):").split())
n, m = 1000, 100
print(gcd(n-1, m-1) + 1)

# pprint(seat1(n, m))
# pprint(seat2(n, m))
# print("-"*45)

arr1 = seat1(n, m)
# for i in arr1:
#     print(i)
    
# print("-"*45)

arr2 = seat2(n, m)
# for i in arr2:
#     print(i)

print(count_students_in_same_seat(n, m))


