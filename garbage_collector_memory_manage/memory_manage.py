import sys

class Order:

    def __del__(self):
        print('Order will be deleted')


a =Order()
print(sys.getrefcount(a))

b = a


print(sys.getrefcount(a))

del b

print(sys.getrefcount(a))