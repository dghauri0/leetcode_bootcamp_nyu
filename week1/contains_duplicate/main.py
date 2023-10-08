from solution import Solution

sol = Solution()

if __name__ == '__main__':
    test0 = [1,2,3,1]
    test1 = [1,2,3,4]
    test2 = [1,1,1,3,3,4,3,2,4,2]
    print(sol.containsDuplicate(test0))
    print(sol.containsDuplicate(test1))
    print(sol.containsDuplicate(test2))

