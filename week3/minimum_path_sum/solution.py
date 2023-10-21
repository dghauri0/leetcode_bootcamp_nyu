from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)  # Rows
        n = len(grid[0])  # Columns
        min_trav_grid_dp = [[float("inf")] * (n + 1) for i in range(m + 1)]
        min_trav_grid_dp[m][n - 1] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_trav_grid_dp[i][j] = min(min_trav_grid_dp[i][j + 1], min_trav_grid_dp[i + 1][j]) + grid[i][j]

        return int(min_trav_grid_dp[0][0])
