from typing import List, Optional
from Trie import Trie


# Given an m x n board of characters and a list of strings words,
# return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Output array.
        output = []

        # Initialize and populate Trie for word list.
        word_trie = Trie()
        for i in words:
            word_trie.insert(i)

        board_visited = [[False] * len(board[0]) for i in range(len(board))]
        # print(board_visited)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_word = ""
                if not board_visited[i][j]:
                    b_i = i
                    b_j = j
                    board_visited[i][j] = True
                    dict = word_trie.query(board[i][j])
                    if len(dict) != 0:
                        curr_word += board[i][j]

                    flag_right_nf = False
                    flag_left_nf = False
                    flag_down_nf = False
                    flag_up_nf = False
                    while (not flag_right_nf or not flag_left_nf or not flag_down_nf or not flag_up_nf) and len(dict) != 0:
                        try:
                            if board[b_i][b_j + 1]:
                                b_j += 1
                                if len(word_trie.query(curr_word + board[b_i][b_j])) == 0:
                                    b_j -= 1
                                    flag_right_nf = True
                                else:
                                    curr_word += board[b_i][b_j]
                        except IndexError:
                            # Index out of bound
                            flag_right_nf = True
                        if board[b_i][b_j - 1]:
                            b_j -= 1
                            if len(word_trie.query(curr_word + board[b_i][b_j])) == 0:
                                b_j += 1
                                flag_left_nf = True
                            else:
                                curr_word += board[b_i][b_j]
                        try:
                            if board[b_i + 1][b_j]:
                                b_i += 1
                                if len(word_trie.query(curr_word + board[b_i][b_j])) == 0:
                                    b_i -= 1
                                    flag_down_nf = True
                                else:
                                    curr_word += board[b_i][b_j]
                        except IndexError:
                            flag_down_nf = True
                        if board[b_i - 1][b_j]:
                            b_i -= 1
                            if len(word_trie.query(curr_word + board[b_i][b_j])) == 0:
                                b_i += 1
                                flag_up_nf = True
                            else:
                                curr_word += board[b_i][b_j]

                        #dict = word_trie.query(curr_word)

                        if words.__contains__(curr_word):
                            output.append(curr_word)
                            # Maybe remove (pop) word from trie
                            break

        return output