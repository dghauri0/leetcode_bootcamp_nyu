from typing import List


# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_edge = 0
        right_edge = len(height) - 1
        output = -1

        # Move edges closer together and calculate max capacity.
        while left_edge < right_edge:

            # Calculate distance between container edges.
            distance = right_edge - left_edge

            # What is the non-slanted container height.
            height_container = min(height[left_edge], height[right_edge])

            # Update maxArea if the area is greater than the previous maxArea calc.
            if distance * height_container > output:
                output = distance * height_container

            # Move edges closer.
            if height[left_edge] < height[right_edge]:
                left_edge = left_edge + 1
            else:
                right_edge = right_edge - 1

        return output