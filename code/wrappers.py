# this file is part of the codebase for a Python project
# NOTE: This script does not perform any file operations. 
# If you encounter FileNotFoundError, check your execution environment or other scripts.
import asyncio
from functools import wraps
import time
import inspect


def retry(func):
    """try to recall func if returns None
    Args:
        *args: Arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try_count = 0
        while try_count < 3 and result is None:
            print(f"Retrying call function {func.__name__}..{try_count} time.")
            time.sleep(1)
            result = func(*args, **kwargs)
            try_count += 1
        return result
    return wrapper


def retry_param(times=3):
    def decorator(func):
        """try to recall func if returns None
        Args:
            *args: Arguments to pass to the function
            **kwargs: Keyword arguments to pass to the function
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try_count = 0
            while try_count < times and result is None:
                print(f"Retrying call function {func.__name__}..{try_count} time.")
                time.sleep(1)
                result = func(*args, **kwargs)
                try_count += 1
            return result
        return wrapper
    return decorator


@retry_param(times=5)
def my_function(x):
    """Function that returns None if x is less than 5, otherwise returns x
    Args:
        x (int): Input value
    Returns:
        int or None: Returns x if x >= 5, otherwise None
    """
    if x < 5:
        return None
    return x


def rerun_gen(param=10):
    """Decorator: rerun generator's next() if value < 10, until value >= 10 or StopIteration."""
    def decorator(func):
        """Decorator: rerun generator's next() if value < 10, until value >= 10 or StopIteration."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            while True:
                try:
                    value = next(gen)
                    while value < param:
                        print(f"Value {value} < {param}, rerunning next()...")
                        value = next(gen)
                    yield value
                except StopIteration:
                    break
        return wrapper
    return decorator


# Пример использования:
@rerun_gen(param=20)
def digen(num=1):
    """ returns generator comprehension square of nums digits of a number"""
    # This is a generator comprehension that generates the square of each digit in the number
    # The walrus operator (:=) is used to assign the square of the digit to 'squared'
    # and then yield it
    for digit in range(1, num):
        squared = int(digit) ** 2
        yield squared


def async_retry(times=3, delay=1):
    """Decorator for async functions: retries if result is None."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try_count = 0
            result = await func(*args, **kwargs)
            while try_count < times and result is None:
                print(f"Async retry {try_count + 1}/{times} for {func.__name__}")
                await asyncio.sleep(delay)
                result = await func(*args, **kwargs)
                try_count += 1
            return result
        return wrapper
    return decorator


# Example usage:
@async_retry(times=3, delay=1)
async def async_example(x):
    print(f"Running async_example with x={x}")
    if x < 5:
        return None
    return x


def async_gen_try_except(func):
    """Decorator: works for both async generators and async functions, catches exceptions and prints error."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            if inspect.isasyncgen(result):
                async for value in result:
                    yield value
            else:
                return
        except Exception as e:
            print(f"Exception in async function/generator '{func.__name__}': {e}")
            if inspect.isasyncgenfunction(func):
                return
            return
    return wrapper


# def try_except(func):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         print(f"Execution '{func.__name__}' with args={args}, kwargs={kwargs}")
#         try:
#             result = await func(*args, **kwargs)
#             return result
#         except Exception as e:
#             print(f"Exception in async function '{func.__name__}': {e}")
#             return
#     return wrapper

# def try_except(func):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         print(f"Execution '{func.__name__}' with args={args}, kwargs={kwargs}")
#         try:
#             result = func(*args, **kwargs)
#             if inspect.isasyncgen(result):
#                 async for value in result:
#                     yield value
#         except Exception as e:
#             print(f"Exception in async function '{func.__name__}': {e}")
#             if inspect.isasyncgenfunction(func):
#                 return
#     return wrapper


def try_except(func):
    # Проверяем тип оригинальной функции один раз при применении декоратора
    if inspect.isasyncgenfunction(func):
        # Эта обертка для асинхронных генераторов
        @wraps(func)
        async def async_gen_wrapper(*args, **kwargs):
            print(f"Execution (async_gen) '{func.__name__}' with args={args}, kwargs={kwargs}")
            try:
                async for value in func(*args, **kwargs):
                    yield value
            except Exception as e:
                print(f"Exception in async generator '{func.__name__}': {e}")
                return
        return async_gen_wrapper
    else:
        # Эта обертка для обычных асинхронных функций
        @wraps(func)
        async def async_func_wrapper(*args, **kwargs):
            print(f"Execution (async_func) '{func.__name__}' with args={args}, kwargs={kwargs}")
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                print(f"Exception in async function '{func.__name__}': {e}")
                return None
        return async_func_wrapper


# Example usage:
@try_except
async def foo3(num):
    for x in range(num):
        if x == 10:
            raise ValueError("Test error at x=3")
        yield x


@try_except
async def foo4(num):
    if num == 10:
        raise ValueError(f"Test error at num = {num}")
    print(num)


async def main():
    print("foo3: =======")
    async for val in foo3(5):
        print(val)
    print("foo4: ========")
    await foo4(10)  # Now works for async function


if __name__ == "__main__":
    # Test for retry decorator
    # print(my_function(3))  # Should retry and return None
    # print(my_function(6))  # Should return 6 without retrying
    # Test for retry_param decorator
    # print(digen(5))  # Should return a generator object
    # return square from digen
    # for i in digen(10):
    #     print(i)  # Should print the square of each digit from 1 to 4

    asyncio.run(main())
