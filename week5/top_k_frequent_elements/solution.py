from typing import List

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        curr_num = nums[0]
        curr_count = 0
        for i in range(len(nums)):
            if nums[i] == curr_num:
                curr_count += 1
            else:
                counts[curr_num] = curr_count
                curr_num = nums[i]
                curr_count = 1

            # Edge case for last element in array
            if i == len(nums) - 1:
                counts[curr_num] = curr_count

        output = []
        k_count = 0
        for key, val in counts.items():
            if k_count < k:
                output.append(key)
                k_count += 1

        return output

