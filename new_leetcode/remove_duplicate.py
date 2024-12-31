"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following 
things:

Change the array nums such that the first k elements of nums contain the unique elements in the order 
they were present in nums initially. The remaining elements of nums are not important as well as the 
size of nums.
Return k.
Custom Judge:
Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 1
        for curr in range(1, len(nums)):
            if nums[curr] != nums[curr-1]:
                nums[pos] = nums[curr]
                pos +=1
            print(nums)
            print(f"result len:{pos}")
        return pos
            
if __name__ == "__main__":
    
    res = Solution()
    nums = [0, 1, 2, 2, 2, 3, 3, 3, 4,  4, 6, 6, 6, 8, 10, 10]
    
    result = res.removeDuplicates(
        nums
    )
    print(f"result list: {nums[:result]}")
                
        