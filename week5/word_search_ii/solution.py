from typing import List, Optional
from Trie import Trie


# Given an m x n board of characters and a list of strings words,
# return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Initialize and populate Trie for word list.
        word_trie = Trie()
        for i in words:
            word_trie.insert(i)

        board_visited = [[False] * len(board[0]) for i in range(len(board))]
        # print(board_visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not board_visited[i][j]:
                    board_visited[i][j] = True
                    
        return None



