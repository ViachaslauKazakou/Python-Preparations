import time
import random

class RetryContextManager:
    def __init__(self, retries):
        self.retries = retries

    def __enter__(self):
        self.attempt = 0
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.attempt += 1
            if self.attempt < self.retries:
                print(f"Attempt {self.attempt}: Failed - Exception: {exc_value}")
                time.sleep(1)  # Optional: wait 1 second before retrying
                return True  # Suppress the exception and retry
            else:
                print(f"All {self.retries} attempts failed.")
                return False  # Do not suppress the exception after max retries
        else:
            print(f"Attempt {self.attempt + 1}: Success - Result: {exc_value}")
            return False  # No exception, do not suppress

def example_function(x):
    if x < 0.5:
        raise ValueError("x is too small")
    return x * 2

if __name__ == "__main__":
    with RetryContextManager(retries=10) as retry:
        while retry.attempt < retry.retries:
            try:
                result = example_function(random.random())
                print(f"Final result: {result}")
                break
            except Exception as e:
                if not retry.__exit__(type(e), e, e.__traceback__):
                    break