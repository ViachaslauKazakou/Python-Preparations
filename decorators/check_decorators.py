from functools import wraps
import time


class Timer:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.start = time.time()
        result = self.func(*args, **kwargs)
        self.end = time.time()
        print(f'{self.func.__name__} took {self.end - self.start} seconds')
        return result


timer = Timer

# decorators with params
def timeit_with_params(param=None):
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'Function {func.__name__} took {end} with params={param}')
            return result
        return wrapper
    return timeit
@timer
def myfunc(t_sleep):
    time.sleep(t_sleep)
    print(f'sleeping {t_sleep} seconds')


@timeit_with_params(param='Decorator with params')
def myfunc2(t_sleep):
    time.sleep(t_sleep)
    print(f'sleeping {t_sleep} seconds')


if __name__ == '__main__':

    myfunc(3)
    myfunc2(5)