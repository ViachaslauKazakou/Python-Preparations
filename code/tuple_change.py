def tuple_ext():
    x = (1, 2, 3, [1, 2])
    try:
        x[3] += [3, 4]
    except Exception as err:
        print(err)
    x[3].extend([5, 6])
    print(x)
    z = [1, 2, 3, 4]
    print(id(z))
    z += [2, 3]
    print(id(z))
    z = z + [6, 7]
    print(z)
    print(id(z))


if __name__ == "__main__":
    tuple_ext()
