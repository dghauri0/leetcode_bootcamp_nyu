from solution import Solution

sol = Solution()

if __name__ == '__main__':
    test0 = [1,3,-1,-3,5,3,6,7]
    k0 = 3
    test1 = [1]
    k1 = 1
    print(sol.maxSlidingWindow(test0, k0))
    print(sol.maxSlidingWindow(test1, k1))



