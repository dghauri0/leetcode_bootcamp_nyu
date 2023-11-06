from solution import Solution

sol = Solution()

if __name__ == '__main__':
    nums_0 = [1]
    k_0 = 1
    nums_1 = [1,2]
    k_1 = 4
    nums_2 = [2,-1,2]
    k_2 = 3
    nums_3 = [77,19,35,10,-14]
    k_3 = 19
    print(sol.shortestSubarray(nums_0, k_0))
    print(sol.shortestSubarray(nums_1, k_1))
    print(sol.shortestSubarray(nums_2, k_2))
    print(sol.shortestSubarray(nums_3, k_3))



