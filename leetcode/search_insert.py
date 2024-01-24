def searchInsert(nums, target):
    check = False
    pos = 0
    for key, i in enumerate(nums):
        if nums[key] >= target:
            pos = key
            check = True
            break
    if check:
        return pos
    else:
        return len(nums)


nums = [1, 3, 5, 6, 7]

print(searchInsert(nums, 5))