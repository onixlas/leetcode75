from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans1 = set(num for num in nums1 if num not in set2)
        ans2 = set(num for num in nums2 if num not in set1)

        return [list(ans1), list(ans2)]
