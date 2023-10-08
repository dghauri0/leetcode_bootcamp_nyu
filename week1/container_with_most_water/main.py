from solution import Solution

sol = Solution()

if __name__ == '__main__':
    height0 = [1,8,6,2,5,4,8,3,7]
    height1 = [1,1]
    height2 = [1,2]
    print(sol.maxArea(height0))
    print(sol.maxArea(height1))
    print(sol.maxArea(height2))
