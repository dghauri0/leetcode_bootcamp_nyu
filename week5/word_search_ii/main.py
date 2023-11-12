from solution import Solution

sol = Solution()

if __name__ == '__main__':
    board_0 = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words_0 = ["oath", "pea", "eat", "rain"]
    board_1 = [["a", "b"], ["c", "d"]]
    words_1 = ["abcb"]
    print(sol.findWords(board_0, words_0))
    print(sol.findWords(board_1, words_1))