
# You are given a parentheses string s. In one move, you can
# insert a parenthesis at any position of the string.
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))"
# or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_open_parenth_count = 0
        right_open_parenth_count = 0
        added = 0

        for i in range(len(s)):
            if s[i] == ')':
                if right_open_parenth_count > left_open_parenth_count:
                    left_open_parenth_count += 1
                else:
                    added += 1

            if s[i] == '(':
                right_open_parenth_count += 1

        added += right_open_parenth_count - left_open_parenth_count

        return added
