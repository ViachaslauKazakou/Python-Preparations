import time


def timer(fn):
    def wrapped(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f"Executive time: {time.time()-start}")
        return result
    return wrapped

@timer
def counter(count:int) -> int:
    return sum([item for item in range(count)])


if __name__ == "__main__":
    print(counter(10000000))
