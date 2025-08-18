import pytest
from src.hashmap_set.find_the_difference_of_two_arrays.solution import Solution


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]), ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []])],
)
def test_find_the_difference_of_two_arrays(nums1, nums2, expected):
    solution = Solution()
    assert solution.findDifference(nums1, nums2) == expected
