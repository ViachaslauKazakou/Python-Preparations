# max_repeat_int(list) находит элемент, который встречается чаще всего в списке.
# Сначала строится словарь, где ключ — элемент списка, а значение — количество его появлений.
# Затем с помощью max(..., key=...) находится ключ с максимальным значением (т.е. наиболее часто встречающийся элемент).
# Функция возвращает этот элемент и его количество.

def max_repeat_int(list):
    max_dict = {}
    for i in list:
        if i in max_dict:
            max_dict[i] += 1
        else:
            max_dict[i] = 1
    max_key = max(max_dict, key=max_dict.get)
    return max_key, max_dict[max_key]
    
    
def max_repeat_int2(lst: list) -> tuple[int, int]:
    # Вызов max(lst, key=lst.count) ищет элемент, для которого lst.count(x) максимально.
    # lst.count(x) возвращает количество вхождений x в список lst.
    # Таким образом, max вернёт элемент, который встречается чаще всего.
    max_elem = max(lst, key=lst.count)
    return max_elem, lst.count(max_elem)


if __name__ == "__main__":
    # Test for max_int
    test_list = [1, 2, 3, 4, 5, 6, 3, 2, 1, 1, 1]
    result = max_repeat_int(test_list)
    print(f"Max int in {test_list} is {result}")
    
    # Test for max_int2
    test_list2 = [1, 2, 3, 4, 5, 6, 3, 2, 1, 1, 1]
    result2 = max_repeat_int2(test_list2)
    print(f"Max int in {test_list2} is {result2}")