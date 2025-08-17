from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num

        return -1
