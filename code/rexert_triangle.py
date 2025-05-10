from random import randint
 
N: int = 5  # Порядок Матрицы
 
# (исходная Матрица)
matr = [[randint(0, 50) for c in range(N)] for r in range(N)]
 
def transp(matr: list):
    """ транспонирование заданной Матрицы """
    for r in range(N):
        for c in range(r + 1, N):
            tmp = matr[c][r]
            matr[c][r] = matr[r][c]
            matr[r][c] = tmp
 
def print_matr(matr: list, name: str):
    """ вывод заданной Матрицы """
    print('\n  ***  ' + name + ':  ***')
    for r in range(N):
        for c in range(N):
            print(f"{matr[r][c]}", end='\t')
        print()
 
# (вывод Матрицы)
print_matr(matr, 'прямая')
 
# (транспонирование Матрицы)
transp(matr)
 
# (вывод Матрицы)
print_matr(matr, 'обратная')