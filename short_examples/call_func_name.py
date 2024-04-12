def func1():
    print("Func1 started")


def func2():
    print("Func2 started")


pipeline = ["func1", "func2"]

# for item in pipeline:
#     globals().get(item)()


current_module = globals()
for item in pipeline:
    func = getattr(current_module, item, None)
    if func and callable(func):
        func()

tuple = {}
tuple[(1,2)] = 8
# print(tuple)


def func3(a, *args, c=None, **kwargs):
    print(args)
    print(kwargs)
    print(a)
    print(c)

if __name__ == "__main__":
    func3(1,2,3,4, b={"q":2}, c=5, x=9)

