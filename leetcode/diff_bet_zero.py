"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
"""

class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        glen = len(grid)
        result = [[] for i in range(glen)]

        for key, item in enumerate(grid):
            print(item)
            k1 = sum(item)
            # for i in item:
            #     print(i)

        for key, item in enumerate(grid):
            o1 = sum(item)
            print(o1)
            # print(key)
            o2 = sum([grid[i][key] for i in range(glen)])
            z1 = len(item) - o1
            z2 = glen - o2
            rz = o1 +o2 - z1 - z2
            result[key].append(rz)
            print(o2)
        print(result)


grid = [[0,1,1],[1,0,1],[0,0,1]]

result = Solution().onesMinusZeros(grid)

print(result)
