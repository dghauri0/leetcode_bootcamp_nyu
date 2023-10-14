class Solution:
    # Goal: Find the length of the longest substring
    #       without repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        right_pointer = len(s)
        while left_pointer < right_pointer:
            
