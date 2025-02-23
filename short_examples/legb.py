import inspect

i = 12

def outer(x):
    def inner():
        y = 7
        z = 10
        print(f'x = {x}')
        print(f'y = {y}')
        print(f'z = {z}')
        print(f'locals = {locals()}')
        print(f'globals = {globals()}')
        print(f'inspect = {inspect.currentframe().f_locals}')
        return x + y + z
    return inner

try:
    # Create closure
    closure_func = outer(5)
    
    # Execute closure
    result = closure_func()
    
    # Inspect closure variables
    closure_vars = inspect.getclosurevars(closure_func)
    print(f'Result = {result}')
    print(f'Closure vars = {closure_vars.nonlocals}')
    
except TypeError as e:
    print(f"TypeError occurred: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
    
def f(v):
    def f1():
        v += 1
        return v+1
    return f1()
 
print(f(2))

