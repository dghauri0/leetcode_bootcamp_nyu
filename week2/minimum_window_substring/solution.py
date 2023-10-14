class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left_pointer = 0
        right_pointer = len(t) - 1
        output = ""
        while right_pointer < len(s):
            for i in range(left_pointer, right_pointer):
                if s[i] in t:
                    output = output + s[i]
            
        return output
