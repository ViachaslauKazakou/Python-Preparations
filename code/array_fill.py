def create_array(n, m):
    # arr = [[i*(j+5) for i in range(n)] for j in range(m)]
    arr = [[i * n + j for i in range(m)] for j in range(n)]

    # arr = [[arr[i * m + j] for j in range(m)] for i in range(n)]
    return arr

if __name__ == "__main__":
    # din = str(input("Введите количество строк, столбцов через пробел: "))
    # n, m = din.split()
    res = create_array(5, 6)
    for item in res:
        print(item)