def timer(func):
    ''' input - function
        output - time of function execution'''
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start:.8f}")
        return result
    return wrapper

@timer
def count_max(nums):
    ''' input - natural number
        output - count of max number in the input'''
    max_num = max(nums)
    return nums.count(max_num)  

@timer
def count2_max(nums):
    ''' input - natural number
        output - count of max number in the input'''
    result = {}
    key = ''
    for num in nums:
        if num > key:
            key = num
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result[str(key)], result

@timer
def count3_max(nums):
    ''' input - sequence of characters/numbers
        output - count of max element in the input'''
    # Pre-allocate dictionary capacity if possible
    result = {}
    max_element = None
    
    # First pass - build frequency dictionary and track max element
    for num in nums:
        # Update max element (using comparison instead of if statements)
        if max_element is None or num > max_element:
            max_element = num
            
        # Update count (using dict.get with default value to avoid condition)
        result[num] = result.get(num, 0) + 1
    
    return result[max_element], result

@timer
def count4_max(n):
    m=0
    nn=n
    while(nn>0):
        k=nn%10
        if k>m : m=k
        nn=nn//10
    nn=n
    c=0
    while(nn>0):
        k=nn%10
        if k==m : c+=1
        nn=nn//10
    return c

@timer
def count_stream_max(nums):
    ''' input - sequence of characters/numbers
        output - count of max element in the input'''
    # Fast path for empty input
    if not nums:
        return 0, {}
    
    # Single-pass algorithm to count frequencies and track max
    counter = {}
    max_element = nums[0]  # Initialize with first element
    
    for num in nums:
        # Update max element in O(1) time
        if num > max_element:
            max_element = num
        
        # Update counter in O(1) amortized time
        counter[num] = counter.get(num, 0) + 1
    
    return counter[max_element]
    

if __name__ == "__main__":
    nums = '122334566788999777457356856845643653838492673408296724039679763298674467348967328097638926734289076348027623089679384673498674865342346687976435813524368808067863254327685678793543654865987595673462645764576487976956376837658847'
    print(count_max(nums))  # 1
    print("-"*50)
    print(count2_max(nums))  # 1
    print("-"*50)
    print(count3_max(nums))  # 1
    print("-"*50)
    print(count4_max(int(nums)))  # 1
    print("-"*50)
    print(count_stream_max(nums))  # 1