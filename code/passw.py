from functools import wraps
from getpass import getpass  # чтобы пароль был невидим


def require_password(correct_password):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            entered = getpass("Введите пароль: ")
            if entered == correct_password:
                return func(*args, **kwargs)
            else:
                print("❌ Неверный пароль. Доступ запрещён.")
        return wrapper
    return decorator

@require_password("1234")
def fibonacci(n):
    def fib_inner(k):
        if k <= 1:
            return k
        return fib_inner(k - 1) + fib_inner(k - 2)
    
    result = fib_inner(n)
    print(f"F({n}) = {result}")

if __name__ == "__main__":
    n = int(input("Введите число для вычисления Фибоначчи: "))
    fibonacci(n)
