from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)  # Rows
        n = len(grid[0])  # Columns

        # Initialize our computation grid with initial infinity values.
        min_trav_grid_dp = [[float("inf")] * (n + 1) for i in range(m + 1)]

        # Set start comparison value to zero near bottom right.
        min_trav_grid_dp[m][n - 1] = 0

        # Iterate backwards through 2D computation grid running computation of
        # minimum of values between the adjacent elements to right and bottom
        # of element under evaluation. Add minimum to original grid at that location.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_trav_grid_dp[i][j] = min(min_trav_grid_dp[i][j + 1], min_trav_grid_dp[i + 1][j]) + grid[i][j]

        # Our answer is in the [0, 0] location.
        return int(min_trav_grid_dp[0][0])
