from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        zero_counter = 0

        for index in range(len(nums)):
            if nums[index] == 0:
                zero_counter += 1
            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1

            max_length = max(max_length, index - left + 1)

        return max_length
