from typing import List
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = ()
        for k in range(len(nums)):
            for key in range(k+1, len(nums)):
                if nums[k] + nums[key] == target:
                    result = (k, key)
                    return result
        return result



nums = [2,5,5,11]
target = 10

print(Solution().twoSum(nums, target))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 5, 5, 11, 4]
    target = 6
    res = Solution().twoSum(nums, target)
    print(res)