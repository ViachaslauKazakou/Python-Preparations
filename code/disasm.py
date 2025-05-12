import dis


def example(x):
    return x + 1


if __name__ == "__main__":
    dis.dis('example(x)')
