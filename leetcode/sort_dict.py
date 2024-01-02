# Sort the dictionary by values in descending order

my_dict = {'a': 4, 'b': 7, 'c': 2, 'd': 5}

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print(sorted_dict_desc)


ls = ['5', '3', '5', 6, 7, '8', 9, 1]
rs = list(set(ls))
print(rs)
