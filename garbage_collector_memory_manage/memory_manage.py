import sys


class Order:

    def __del__(self):
        print('Order will be deleted')


a = Order()

print(sys.getrefcount(a))

b = a

c = a

print(sys.getrefcount(a))
print("-"*100)

del b

print(sys.getrefcount(a))

del c

print(sys.getrefcount(a))