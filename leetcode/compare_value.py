def compare(first, second):

    points = {"A": 1, "B": 3, "C": 5}

    res = lambda s:  sum(points[val] for val in s)

    f_score = res(first)
    s_score = res(second)
    print(res(first))
    print(res(second))

    if f_score > s_score:
        return "First"
    elif f_score < s_score:
        return "Second"
    else:
        return "Tie"


if __name__ == "__main__":
    bob = "BBACB"
    erica = "BCBAB"
    print(compare(bob, erica))