
from contextlib import contextmanager


@contextmanager
def mymanager():
    try:
        print("entering mymanager")
        yield "To do something"
    finally:
        print("exiting mymanager")


class ContextManager:

    def __init__(self):
        pass

    def __enter__(self):
        print("start session")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end session")
        return False


@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()


def myfunc():
    with ContextManager() as manager:
        print("start func")

def myfunc2():
    with mymanager() as manager:
        print("start")

if __name__ == "__main__":

    myfunc()
    print("-------- Start 2nd function -------")
    myfunc2()