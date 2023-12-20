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
print(tuple)


def func3(*args, **kwargs):
    print(args)
    print(kwargs)


func3(12,12, x=5)