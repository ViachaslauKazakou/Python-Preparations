import multiprocessing
import os
import time
import random
from functools import wraps


def timer(func):
    # @wraps
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result

    return wrapper


def square(number):
    """Function to compute square of a number."""
    print(f"start process with {number}")
    time.sleep(1)
    return number * number


@timer
def run_process():
    print(f"start process with {os.getpid()}")
    numbers = (random.randint(1, 10) for _ in range(100))
    pool = multiprocessing.Pool(processes=8)
    results = pool.map(square, numbers)
    # Close the pool
    pool.close()
    pool.join()
    return results


if __name__ == "__main__":
    result = run_process()

    # Output the results
    # print("Original numbers:", numbers)
    print("Squared numbers:", len(result))
