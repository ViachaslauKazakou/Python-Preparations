import threading
import os
import time
import random
from functools import wraps
import concurrent.futures


def timer(func):
    @wraps(func)
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
    time.sleep(2)
    return number * number


@timer
def run_thread():
    print(f"start process with {os.getpid()}")
    numbers = (random.randint(1, 10) for _ in range(100))
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        # Submit tasks to the executor and retrieve futures
        futures = [executor.submit(square, num) for num in numbers]

        # Wait for all tasks to complete and retrieve results
        results = [
            future.result() for future in concurrent.futures.as_completed(futures)
        ]

    return results


if __name__ == "__main__":
    result = run_thread()

    # Output the results
    # print("Original numbers:", numbers)
    print("Squared numbers:", len(result))
