from solution import Solution

sol = Solution()

if __name__ == '__main__':
    s_0 = "())"
    s_1 = "((("
    s_2 = "()))(("
    print(sol.minAddToMakeValid(s_0))
    print(sol.minAddToMakeValid(s_1))
    print(sol.minAddToMakeValid(s_2))



