from solution import Solution

sol = Solution()

if __name__ == '__main__':
    grid0 = [[1,3,1],[1,5,1],[4,2,1]]
    grid1 = [[1,2,3],[4,5,6]]
    print(sol.minPathSum(grid0))
    print(sol.minPathSum(grid1))

