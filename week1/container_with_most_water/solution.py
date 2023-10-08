from typing import List


# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        output = -1
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                distance = j - i
                if min(height[j], height[i]) * distance > output:
                    output = min(height[j], height[i]) * distance

        return output
