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
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates in-place from a sorted array.
        
        Args:
            nums: Sorted array of integers
            
        Returns:
            Number of unique elements
            
        Examples:
            >>> s = Solution()
            >>> nums = [1,1,2]
            >>> k = s.removeDuplicates(nums)
            >>> nums[:k]
            [1,2]
        """
        if not nums:
            return 0
            
        if len(nums) == 1:
            return 1
            
        # Position for next unique element
        write_pos = 1
        
        try:
            # Iterate through array starting from second element
            for read_pos in range(1, len(nums)):
                if nums[read_pos] != nums[read_pos - 1]:
                    nums[write_pos] = nums[read_pos]
                    write_pos += 1
                    
            return write_pos
            
        except Exception as e:
            print(f"Error processing array: {e}")
            return 0


def main():
    # Test cases
    test_cases = [
        [0,0,1,1,1,2,2,3,3,4],
        [1,1,2],
        [],
        [1]
    ]
    
    solution = Solution()
    
    for nums in test_cases:
        k = solution.removeDuplicates(nums)
        print(f"Input: {nums}")
        print(f"Unique elements: {k}")
        print(f"Modified array first {k} elements: {nums[:k]}\n")


if __name__ == "__main__":
    main()