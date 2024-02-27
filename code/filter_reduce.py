from functools import reduce

# Фильтрация списка чисел, оставляем только четные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# Сокращение списка чисел до их суммы
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # 15


from functools import reduce

# Итерируемый объект со строками
strings = ["apple", "banana", "cherry", "date", "elderberry"]

# Фильтруем строки, начинающиеся с буквы "a"
a_strings = list(filter(lambda x: x.startswith("a"), strings))
print(a_strings)  # ["apple"]

# Склеиваем оставшиеся строки в одну, используя reduce()
result = reduce(lambda x, y: x + y, a_strings)
print(result)  # "apple"

# Также можно записать это все в одну строку
result = reduce(lambda x, y: x + y, filter(lambda x: x.startswith("a"), strings))
print(result)  # "apple"
