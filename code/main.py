import time
import threading
import concurrent.futures

import time


def timerp(repeat=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(repeat):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total_time += end - start
            average_time = total_time / repeat
            print(f"Average execution time ({repeat} times): {average_time:.6f} seconds")
            return result
        return wrapper
    return decorator

# Пример использования:


@timerp(repeat=3)  # Задайте количество повторений
def some_function(param1, param2):
    # Ваша функция
    time.sleep(1)
    return param1 + param2

result = some_function(5, 10)
print("Result:", result)



def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Executive time: {time.time()-start}")
        return result

    return wrapper


def fibbonachi(num):
    if num in {0, 1}:
        return 1
    return fibbonachi(num - 2) + fibbonachi(num - 1)


@timer
def fb(num):
    return fibbonachi(num)


@timer
def fb_thread(num):
    if num < 2:
        return 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(fibbonachi, [num - 2, num - 1]))

    return sum(results)


@timer
def fb_process(num):
    if num < 2:
        return 1

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fibbonachi, [num - 2, num - 1]))

    return sum(results)


if __name__ == "__main__":
    num = 20
    print(fb_process(num))
    print("-" * 40)

    print(fb_thread(num))
    print("-" * 40)
    print(fb(num))
