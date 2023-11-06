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
    nums_4 = [17,85,93,-45,-21]
    k_4 = 150
    nums_5 = [84,-37,32,40,95]
    k_5 = 167
    print(sol.shortestSubarray(nums_0, k_0))
    print(sol.shortestSubarray(nums_1, k_1))
    print(sol.shortestSubarray(nums_2, k_2))
    print(sol.shortestSubarray(nums_3, k_3))
    print(sol.shortestSubarray(nums_4, k_4))
    print(sol.shortestSubarray(nums_5, k_5))



