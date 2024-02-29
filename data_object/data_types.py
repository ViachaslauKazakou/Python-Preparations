import sys
from functools import wraps

l =[]


def delimiter(delimiter="-"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(delimiter*100)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def func():
    for i in range(5):
        l.append(i)
        print(sys.getsizeof(l))

@delimiter(delimiter="-")
def compare(data1,data2):
    a = data1
    b = data2
    print(f'Compare data: data={data1}/{data2} with len={len(str(data1))}')
    print(a is b)
    print(f"ID a = {id(a)}; ID B = {id(b)}")


if __name__ == '__main__':
    print(sys.argv)
    func()
    compare(100000000000,100000000000)
    compare("this is long string for compare elements", "this is long string for compare elements")
    compare([1,2,3,4,5,6,7], [1,2,3,4,5,6,7])
    a = {1:"2"}
    compare({1:"2"}, {1:"2"})