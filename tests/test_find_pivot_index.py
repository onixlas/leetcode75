import pytest
from src.prefix_sum.find_pivot_index.solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0)],
)
def test_find_pivot_index(nums, expected):
    solution = Solution()
    assert solution.pivotIndex(nums) == expected
