import time
from functools import wraps

def retry_wrapper(retries):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    result = func(*args, **kwargs)
                    print(f"Attempt {attempt}: Success - Result: {result}")
                    return result
                except Exception as e:
                    print(f"Attempt {attempt}: Failed - Exception: {e}")
                    time.sleep(1)  # Optional: wait 1 second before retrying
            print(f"All {retries} attempts failed.")
            return None
        return wrapper
    return decorator

@retry_wrapper(retries=10)
def example_function(x):
    if x < 0.5:
        raise ValueError("x is too small")
    return x * 2

if __name__ == "__main__":
    import random
    result = example_function(random.random())
    print(f"Final result: {result}")