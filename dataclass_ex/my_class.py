from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DClass:
    get_one: Any = "12345"
    return_value: Any = None

    def __call__(self, *args, **kwargs):
        return self.get_one

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return None

class DT:

    def __init__(self, get_one=None, return_value=None):
        self.get_one = get_one
        self.return_value = return_value

    def __call__(self, *args, **kwargs):
        return self.get_one

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return None


def wrap_func():
    return DClass


def my_func():
    with DClass() as session:
        print("start")
        print(session.get_one)


def func():
    return "func"


if __name__ == "__main__":

    res = wrap_func()(get_one=1)
    res.get_one = 1
    print(res)
    print(res.get_one)
    print(res.return_value)

