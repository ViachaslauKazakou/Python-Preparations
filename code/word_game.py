from itertools import permutations
import math

def variants(word, length, start):
    n = len(word)
    r = length
    num_permutations = math.factorial(n) // math.factorial(n - r)
    
    print(f"Варианты слов из {length} букв, начинающиеся на {start}: {num_permutations}")
    
    for word in permutations(word, lenght):
        res = ''.join(word)
        if res.startswith(start):
            print(res)

        
if __name__ == '__main__':
    word = 'бнзрао'
    print(sorted(word))
    lenght = 5
    start = "о"
    variants(word, lenght, start)