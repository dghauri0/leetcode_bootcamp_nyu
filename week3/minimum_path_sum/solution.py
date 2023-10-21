from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        sum = float("inf")
        local_sum = 0
        print(sum)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                local_sum += grid[i][j]
