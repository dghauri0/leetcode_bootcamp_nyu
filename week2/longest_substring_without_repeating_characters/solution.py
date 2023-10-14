class Solution:
    # Goal: Find the length of the longest substring
    #       without repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        left_pointer = 0
        output = 0
        for right_pointer in range(len(s)):
            while s[right_pointer] in chars:
                chars.remove(s[left_pointer])
                left_pointer = left_pointer + 1
            chars.append(s[right_pointer])
            output = max(output, right_pointer - left_pointer + 1)
        return output



