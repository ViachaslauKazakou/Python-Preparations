"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_sum = 0
        while j < len(prices):
            if prices[i] >= prices[j]:
                i = j

            else:
                val = prices[j] - prices[i]
                max_sum = max(max_sum, val)
            j += 1
        return max_sum
                

prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
