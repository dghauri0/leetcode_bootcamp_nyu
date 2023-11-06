from typing import List

# Given an integer array nums and an integer k,
# return the length of the shortest non-empty subarray of nums
# with a sum of at least k. If there is no such subarray, return -1.

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        output = -1
        sum = 0
        count = 0

        for i in range(len(nums)):
            if sum <= k:
                sum += nums[i]
                count += 1

        if sum >= k:
            output = count

        return output