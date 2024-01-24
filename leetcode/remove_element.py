nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val):

    res = []
    check = 0
    for i in nums:
        if i != val:
            res.append(i)
        else:
            check +=1
    for x in range(check):
        nums.remove(val)
    return check

print(removeElement(nums, val))
print(nums)