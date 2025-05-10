def min_array_elem():
    """
    input array from input.
    convert array to dict using fromkeys
    find index min elem using dict
    """
    # input array
    arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
    # convert to dict
    d = dict(enumerate(arr))

    min_index = min(d, key=d.get)
    print(f"Min element is {d[min_index]} at index {min_index}")
    
    
def var2():
    # The lambda in min(enumerate(arr), key=lambda pair: pair[1]) is used to extract the value from each (index, value) pair.
    # min() will return the (index, value) pair with the smallest value in the array.
    arr = list(map(int, input().split()))
    print([x for x in enumerate(arr)])
    print(min(enumerate(arr), key=lambda pair: pair[1]))


if __name__ == "__main__":
    var2()
    