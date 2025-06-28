import time

nums = [123, 45, 678, 90, 12345, 3445, 4456, 455567, 6789, 1234567890, 12345678901234567890, 123456789012345678901234567890, 1234567890123456789012345678901234567890]


def timer(retries=1):
    '''Decorator to measure average execution time of a function over `retries` runs'''
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            print(f"Function '{func.__name__}' starts measuring time")
            for _ in range(retries):
                start_time = time.time()
                result = func(*args, **kwargs)
                print("-" * 20)
                end_time = time.time()
                total_time += (end_time - start_time)
            avg_time = total_time / retries
            print(f"Function '{func.__name__}' average execution time over {retries} runs: {avg_time:.8f} seconds")
            return result
        return wrapper
    return decorator


@timer(retries=3)
def func1(nums):
    result = {
        i: f'{nums}'.count(i)
        for i in '0123456789'
        if i in f'{nums}'
    }
    print(*result.items(), sep="\n")


@timer(retries=3)
def func2(nums):
    s = str(nums)
    result = {
        i: s.count(i)
        for i in '0123456789'
        if i in s
    }
    print(*result.items(), sep="\n")

@timer(retries=3)
def func3(nums):
    s = f"{nums}"
    result = {
        i: s.count(i)
        for i in '0123456789'
        if i in s
    }
    print(*result.items(), sep="\n")

@timer(retries=3)
def foo(lst):
    acc=[0]*10
    for num in lst:
        while num > 0:
            k = num % 10
            acc[k] += 1
            num = num // 10
    for i in range(10):
        print((i, acc[i]))

@timer(retries=3)
def count(nums):
    '''Count the number of digits in a list of numbers'''
    result = {}
    for num in nums:
        for digit in str(num):
            if digit in result:
                result[digit] += 1
            else:
                result[digit] = 1
    print(*result.items(), sep="\n")
  
    
@timer(retries=3)
def count2(nums):
    '''Count the number of digits in a list of numbers'''
    result = {}
    num_list = f"{nums}"
    for item in num_list:
        if item.isdigit():
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    print(*result.items(), sep="\n")
 

if __name__ == "__main__":
    count2(nums)
    foo(nums)

        # foo(nums)
        # func1(nums)
        # func2(nums)
        # func3(nums)
