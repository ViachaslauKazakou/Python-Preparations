

def list_conv(l: list) -> list:
    res = l[:]

    res[0] = "33"
    l[0] = "33"
    return res

#non-local(enclosure)
#

def outer_function():
    outer_variable = 20

    def inner_function():
        print(outer_variable)

        nonlocal a
    inner_function()  # Выведет: 20

outer_function()

# global
global_variable = 30

def global_function():
    print(global_variable)

global_function()  # Выведет: 30



if __name__ == "__main__":
    l = [1,2,3,4,]

    result = list_conv(l)

    print(l)
    print(result)

    print(result == l)
    print(l is result)
