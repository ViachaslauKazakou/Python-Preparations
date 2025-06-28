# n = int(input(" "))

# This is a complex list comprehension that does several things:
result = [
    # For each filtered list of even numbers:
    # 1. Create a list of squares using the walrus operator to store it in 'squared'
    # 2. Unpack the squares list with * operator
    # 3. Add the sum of the original numbers at the end
    [*(squared := [int(i) ** 2 for i in nums]), sum(int(i) for i in nums)]
    
    # This part generates 3 lists by:
    # 1. Prompting user for input 3 times (range(3))
    # 2. Splitting each input by commas
    # 3. Filtering to keep only even numbers
    for nums in [[i for i in input(f"Enter list {_}: ").split(",") if int(i) % 2 == 0] for _ in range(3)]
    
    # Only process non-empty lists
    if nums
]
print(result)
