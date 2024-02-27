count = sum(1 for line in open('filename.txt') for c in line if c.isupper())
print(count)

string1 = "emansipation"
string2 = "hello"

# Создадим множества символов из строк
set1 = set(string1)
set2 = set(string2)

# Найдем общие символы
common_characters = set1.intersection(set2)

# Преобразуем общие символы обратно в строку
result = ''.join(common_characters)

print(result)