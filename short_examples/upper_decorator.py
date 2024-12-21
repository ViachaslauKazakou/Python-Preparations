from functools import wraps

def upper_data(func):
    """Decorator that uppercases the data returned by the function

    Args:
        func (function): Function to be decorated

    Returns:
        function: Decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return data.upper()
    return wrapper

@upper_data
def my_coll(*args, **kwargs):
    """Return list if received args else dict if receive dict. Print type of received data

    Returns:
        list or dict: Depending on the input
    """
    print("Received type:", "list" if args else "dict" if kwargs else "none")
    return list(args) if args else kwargs if kwargs else None

if __name__ == '__main__':
    my_dict = {"a": 1, "b": 2, "c": 3}
    mycoll = my_coll(**my_dict)
    print(mycoll)

    data = ["name", "list", "nobody"]
    mycoll = my_coll(*data)
    print(mycoll)
