from solution import Solution

sol = Solution()

if __name__ == '__main__':
    nums_0 = [1,1,1,2,2,3]
    k_0 = 2
    nums_1 = [1]
    k_1 = 1
    nums_2 = [3,0,1,0]
    k_2 = 1
    nums_3 = [4,1,-1,2,-1,2,3]
    k_3 = 2
    print(sol.topKFrequent(nums_0, k_0))
    print(sol.topKFrequent(nums_1, k_1))
    print(sol.topKFrequent(nums_2, k_2))
    print(sol.topKFrequent(nums_3, k_3))



