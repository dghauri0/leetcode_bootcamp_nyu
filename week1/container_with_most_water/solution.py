from typing import List


# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Sort the integer list.
        height.sort()

        output = -1
        for i in reversed(range(len(height))):
            if i != 0:
                if height[i] == height[i - 1]:
                    output = height[i] * height[i - 1]
                    return output

        return output