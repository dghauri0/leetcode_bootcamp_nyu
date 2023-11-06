from typing import List

# Given an integer array nums and an integer k,
# return the length of the shortest non-empty subarray of nums
# with a sum of at least k. If there is no such subarray, return -1.

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        sums_global = []
        length_global = []

        while (right < len(nums)):
            sum = 0
            length = -1

            for i in range(left, right + 1):
                sum += nums[i]

            if sum >= k:
                length = (right - left) + 1
                sums_global.append(sum)
                length_global.append(length)

            if sum <= k:
                right += 1
            else:
                left += 1

        try:
            return min(length_global)
        except:
            return -1
