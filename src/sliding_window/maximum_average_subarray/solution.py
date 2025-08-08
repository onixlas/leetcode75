from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_total = total

        for index in range(k, len(nums)):
            total -= nums[index - k]
            total += nums[index]
            max_total = max(total, max_total)

        return max_total / k
