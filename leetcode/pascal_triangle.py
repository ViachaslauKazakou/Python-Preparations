"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

"""

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1], [1, 1]]
        for row in range(1, rowIndex+1):
            print(f"create row {row}")
            print(result[row])
            p_row = result[row].copy()
            p_row.insert(0, 0)
            p_row.append(0)
            print(p_row)
            c_row = []
            for i in range(len(p_row)-1):
                c_row.append(p_row[i]+p_row[i+1])
            result.append(c_row)
        return result[rowIndex]

rowIndex = 4
res = Solution()
print(res.getRow(rowIndex))