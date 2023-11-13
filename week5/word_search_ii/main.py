from solution import Solution

sol = Solution()

if __name__ == '__main__':
    board_0 = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words_0 = ["oath", "pea", "eat", "rain"]
    board_1 = [["a", "b"], ["c", "d"]]
    words_1 = ["abcb"]
    board_2 = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words_2 = ["oa","oaa"]
    board_3 = [["a", "a"]]
    words_3 = ["aaa"]
    print(sol.findWords(board_0, words_0))
    print(sol.findWords(board_1, words_1))
    print(sol.findWords(board_2, words_2))
    print(sol.findWords(board_3, words_3))