from solution import Solution

sol = Solution()

if __name__ == '__main__':
    s0 = "ADOBECODEBANC"
    t0 = "ABC"
    s1 = "a"
    t1 = "a"
    s2 = "a"
    t2 = "aa"
    print(sol.minWindow(s0, t0))
    print(sol.minWindow(s1, t1))
    print(sol.minWindow(s2, t2))
