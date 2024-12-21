def func(n):
    if n == 0:
        return 1
    return n * func(n-1)

print(func(5))

s = '123'
print(list(s))

print(min(max(False, -3, -4), 2, 7))

print(all([]), any([]))

set_ = set()
for i in set_:
    print(False)
print(True)

print("abc DEF".capitalize())

def foo(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)
q = ['abc', 'def']

print(id(q)==foo(q))

class Demo1:
    x = 1
    def __init__(self):
        self.y = 2
        self.x = self.x
        

if __name__ == "__main__":
    foo = Demo1()
    foo.z = 3
    print(len(foo.__dict__))
    print(foo.__dict__)
    print(foo.x)
    print(Demo1.__dict__)

