from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, max_length, zeros_counter = 0, 0, 0

        for index in range(len(nums)):
            if nums[index] == 0:
                zeros_counter += 1
            while zeros_counter > 1:
                if nums[left] == 0:
                    zeros_counter -= 1
                left += 1
            max_length = max(max_length, index - left)
        return max_length
