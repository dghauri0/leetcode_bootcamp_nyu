from solution import Solution

sol = Solution()

if __name__ == '__main__':
    edges_0 = [[1,2],[2,3],[4,2]]
    edges_1 = [[1,2],[5,1],[1,3],[1,4]]
    print(sol.findCenter(edges_0))
    print(sol.findCenter(edges_1))



