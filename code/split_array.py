original_array = [3, -1, 0, 25, -5, 7, -2, 10, -4]
positive_array, non_positive_array = [], []
for x in original_array:
    (positive_array if x > 0 else non_positive_array).append(x)
print(f"Positive array: {positive_array}")
print(f"Non-positive array: {non_positive_array}")