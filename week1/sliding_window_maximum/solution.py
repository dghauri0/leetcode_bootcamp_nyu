import itertools
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left_edge = 0
        right_edge = k - 1
        maximums = deque()
        deqNums = deque(nums)

        # Outer while loop goes through all sliding iterations.
        while right_edge <= len(nums) - 1:
            slice = deque(itertools.islice(deqNums, left_edge, right_edge + 1))
            local_max = max(slice)
            maximums.append(local_max)

            left_edge = left_edge + 1
            right_edge = right_edge + 1

        return maximums
