import dis
import timeit
from math import isqrt

def using_for(n: int) -> bool:
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def using_while(n: int) -> bool:
    i = 2
    max_value = isqrt(n)
    while i <= max_value:
        if n % i == 0:
            return False
        i += 1
    return True

# Compare bytecode
print("For loop bytecode:")
dis.dis(using_for)
print("\nWhile loop bytecode:")
dis.dis(using_while)

# Compare performance
number = 27
for_time = timeit.timeit(lambda: using_for(number), number=1000000)
while_time = timeit.timeit(lambda: using_while(number), number=1000000)

print(f"\nPerformance comparison for n={number}:")
print(f"For loop: {for_time:.6f} seconds")
print(f"While loop: {while_time:.6f} seconds")