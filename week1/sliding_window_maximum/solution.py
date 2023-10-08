from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left_edge = 0
        right_edge = k - 1
        maximums = []

        # Outer while loop goes through all sliding iterations.
        while right_edge <= len(nums) - 1:
            local_max = -1
            for i in range(left_edge, right_edge + 1):
                if nums[i] > local_max:
                    local_max = nums[i]
            maximums.append((local_max))

            left_edge = left_edge + 1
            right_edge = right_edge + 1

        return maximums