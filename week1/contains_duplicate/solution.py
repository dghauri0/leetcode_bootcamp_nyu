from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        output = False
        if len(nums) > 1:
            if nums[0] == nums[1]:
                output = True
                return output
        return output
