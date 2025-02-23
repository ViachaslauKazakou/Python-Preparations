from typing import Generator, Any
from math import isqrt
import timeit
import dis
import cProfile
import pstats
     
        
def sum_for(n: int) -> int:
    res = 0
    for i in range(n):
        res += isqrt(i)
    return res

def sum_while(n: int) -> int:    
    res = 0
    i = 0
    while i < n:
        res += isqrt(i)
        i += 1
    return res

def profile_loops():
    number = 100000
    
    print("\n=== FOR LOOP PROFILE ===")
    cProfile.run('sum_for(1000)', sort='cumtime')
    
    print("\n=== WHILE LOOP PROFILE ===")
    cProfile.run('sum_while(1000)', sort='cumtime')
        
if __name__ == "__main__":
    number = 100000
    print(sum_for(number))
    for_time = timeit.timeit(lambda: sum_for(number), number=1000)
    while_time = timeit.timeit(lambda: sum_while(number), number=1000)
    print("=== FOR LOOP BYTECODE ===")
    dis.dis(sum_for)
    print("=== WHILE LOOP BYTECODE ===")
    dis.dis(sum_while)
    print(f"\nPerformance comparison for n={number}:")
    print(f"For loop: {for_time:.6f} seconds")
    print(f"While loop: {while_time:.6f} seconds")
    profile_loops()