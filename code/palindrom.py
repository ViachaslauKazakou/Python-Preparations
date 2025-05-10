my_text = "AFDGADGHAGHGJAGJ ADGHADGOJAJAG ABDGJHAGDJGAJAHA"


def find_palindrome(base_word):
    
    count = len(base_word)
    word = base_word[:count]
    for i in word:
        print(f"word: {' ' * 9}{word[count:]}")
        print(f"reverted word: {word[count:][::-1]}")
        if word[count:] == word[count:][::-1] and len(word[count:]) > 1: 
            print(f"Found palindrome: {word[count:]}")
        count -= 1


def longest_palindrome(s):
    n = len(s)
    start = 0
    max_length = 1  # Минимальный палиндром — один символ

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # Возвращаем длину и начало палиндрома
        return right - left - 1, left + 1

    for i in range(n):
        # Нечетный палиндром (центр в i)
        length1, start1 = expand_around_center(i, i)
        # Четный палиндром (центр между i и i+1)
        length2, start2 = expand_around_center(i, i + 1)

        # Обновляем максимальную длину и начало
        if length1 > max_length:
            max_length = length1
            start = start1
        if length2 > max_length:
            max_length = length2
            start = start2

    return s[start:start + max_length]


          
if __name__ == "__main__":
    find_palindrome("ABDGGDAHADGAHA")
    # print(f"Longest palindrome: {longest_palindrome}")# Тест
    s = "ABDGGDAHADGAHA"
    result = longest_palindrome(s)
    print("Самый длинный палиндром:", result)
    print("Длина палиндрома:", len(result))
    
    
def all_palindromes(s):
    n = len(s)
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 >= 2:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1

    for i in range(n):
        expand_around_center(i, i)    # Нечетные палиндромы
        expand_around_center(i, i + 1)  # Четные палиндромы

    return sorted(palindromes, key=len, reverse=True)

def longest_palindrome(s):
    n = len(s)
    start, max_length = 0, 1

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1

    for i in range(n):
        length1, start1 = expand_around_center(i, i)
        length2, start2 = expand_around_center(i, i + 1)
        if length1 > max_length:
            max_length, start = length1, start1
        if length2 > max_length:
            max_length, start = length2, start2

    return s[start:start + max_length]

# Тест
s = "ABDGJHAGDJGAJAHA"
palindromes = all_palindromes(s)
print("Все палиндромы (длина ≥ 2):", palindromes)
print("Самый длинный палиндром:", longest_palindrome(s))