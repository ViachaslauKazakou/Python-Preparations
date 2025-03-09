import time
from functools import wraps


def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.8f} seconds to execute")
        return result
    return wrapper


@execution_timer
def count_stream_max_base(nums):
    counter = {}
    max_element = nums[0] 
    
    for num in nums:
        # Update max element in O(1) time
        if num > max_element:
            max_element = num
        
        # Update counter in O(1) amortized time
        counter[num] = counter.get(num, 0) + 1
    
    return counter[max_element]


@execution_timer
def count_stream_max_opt(nums):
    nums = str(nums)
    max_element = nums[0] 
    max_count = 0  # Счётчик количества вхождений максимального элемента
    
    for num in nums:
        if num > max_element:
            max_element = num
            max_count = 1  # Начинаем заново считать максимумы
        elif num == max_element:
            max_count += 1  # Увеличиваем счётчик
    
    return max_count

@execution_timer
def max_dig(n):
    m = 0
    nn = n
    while(nn > 0):
        k = nn % 10
        if k > m : m = k
        nn = nn // 10
    
    nn = n
    c = 0
    while(nn > 0):
        k = nn % 10
        if k == m : c += 1
        nn = nn // 10
    
    return c

@execution_timer
def max_dig_opt(n):
    digs=10*[0]
    while n > 0:
        digs[n%10]+=1
        n=n//10
    i=9
    while digs[i]>0:
        return digs[i]
        i-=1


@execution_timer
def get_count_max_digit(number: int) -> int:
    count = 0
    max_digit = 0
    for dig_str in str(number):
        dig = int(dig_str)
        if dig > max_digit:
            max_digit = dig
            count = 1
        elif dig == max_digit:
            count += 1
    return count


if __name__ == "__main__":
    # Test the decorator
    number = 1287462378562395710957195613634737658653825035023895834906734896739086732849067348926734829791658373763425423623623632004632463878383276478125672385679195729
    print(f"lenght of number: {len(str(number))}")
    print("-"*50)
    print(count_stream_max_base(str(number)))
    print(count_stream_max_opt(number))
    print(max_dig(number))
    print(max_dig_opt(number))
    print(get_count_max_digit(number))
    print(get_count_max_digit("12345678rrr90"))