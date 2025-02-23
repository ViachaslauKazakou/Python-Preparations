import asyncio
import time
from functools import wraps
from typing import Any

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

def func1(key):
    if key:
        print("Start execution")
        test()
        print("End execution")
    else:
        print("Start async execution")
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        loop.create_task(async_test())
        print("End async execution")

def test():
    print("Test started")
    time.sleep(5)
    print("Test completed")

async def async_test():
    print("Async Test started")
    await asyncio.sleep(3)
    print("Async Test completed")

if __name__ == "__main__":
    func1(True)
    print("************************")
    func1(False)
    print("Main program continues immediately after starting async task")
    time.sleep(10)  # Give some time for the async task to complete

