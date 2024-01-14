from functools import wraps
import time
import cProfile


def timer(fn):
    """ This is Simple decorator"""
    @wraps(fn)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f"Executive time: {time.time()-start}")
        return result
    return wrapped


@timer
def counter(count: int) -> int:
    """ Counter with sum """
    res = sum([item for item in range(count)])
    print(f"Result2 = {res}")
    return res


def counter2(count: int) -> int:
    """ Counter2 with sum """
    res = sum([item for item in range(count)])
    print(f"Result2 = {res}")
    return res


def profile(func):
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        print(profile_filename)
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        print(profiler.__dict__)
        return result
    return wrapper

@profile
def counter3(count: int) -> int:
    """ Counter2 with sum """
    res = sum([item for item in range(count)])
    print(f"Result3 = {res}")
    return res


# Пример использования декоратора с параметрами
def profiler_with_params(prefix="Execution"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{prefix}: {func.__name__} took {execution_time:.4f} seconds to execute")
            return result
        return wrapper
    return decorator


@profiler_with_params(prefix="Processing Time")
def example_function():
    """Примерная функция."""
    time.sleep(2)
    print("Function executed")


class TimeProfiler1:
    def __init__(self, func):
        wraps(func)(self)  # Применяем wraps для сохранения метаданных
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{self.func.__name__} took {execution_time:.4f} seconds to execute")
        return result


class Profiler:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{self.func.__name__} took {execution_time:.4f} seconds to execute")
        return result

@Profiler
def pro_function():
    # Ваш код здесь
    time.sleep(2)
    print("Function executed")
    
    
# Пример использования декоратора
@TimeProfiler1
def example_function1():
    """Примерная функция."""
    time.sleep(2)
    print("Function executed")
    

def logger_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("= "*40)
        print(f"Start function {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@logger_func
def dataprint(name):
    print(name)
    
        
if __name__ == "__main__":
    print(timer.__doc__)
    print(counter.__doc__)
    print(counter2.__doc__)
    counter(100000)
    timer(counter2)(100000)
    print("-"*80)
    # counter3(1000)
    print(example_function.__doc__)
    example_function()
    example_function1()
    pro_function()
    dataprint("Slava")