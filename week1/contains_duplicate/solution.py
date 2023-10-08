from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j]:
                        output = True
                        return output
        return output