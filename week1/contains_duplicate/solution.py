from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        output = False
        if len(nums) > 1:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    output = True
                    return output
        return output
