from solution import Solution

sol = Solution()

if __name__ == '__main__':
    s0 = "egg"
    t0 = "add"
    s1 = "foo"
    t1 = "bar"
    s2 = "paper"
    t2 = "title"
    s3 = "badc"
    t3 = "baba"
    print(sol.isIsomorphic(s0, t0))
    print(sol.isIsomorphic(s1, t1))
    print(sol.isIsomorphic(s2, t2))
    print(sol.isIsomorphic(s3, t3))


