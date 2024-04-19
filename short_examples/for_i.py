ls = [1,2,3,4,5,6]

for i in range(1,6):
    print(f" el {i}: {ls[i]}")
    ls[i-1] = ls[i]
    
print(ls)