from typing import List

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Sort nums for easier later dictionary manipulation.
        nums = sorted(nums)
        counts = {}
        curr_num = nums[0]
        curr_count = 0

        # Populate dictionary.
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

        # Get maximum value from dictionary, append key.
        output = []
        for i in range(k):
            key_max = max(counts, key=counts.get)
            output.append(key_max)
            counts.pop(key_max)

        return output

