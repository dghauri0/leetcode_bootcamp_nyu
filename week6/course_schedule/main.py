from solution import Solution

sol = Solution()

if __name__ == '__main__':
    numCourses_0 = 2
    prerequisites_0 = [[1,0]]
    numCourses_1 = 2
    prerequisites_1 = [[1,0],[0,1]]

    print(sol.canFinish(numCourses_0, prerequisites_0))
    print(sol.canFinish(numCourses_1, prerequisites_1))


