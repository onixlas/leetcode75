import pytest
from src.sliding_window.maximum_average_subarray.solution import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [([1, 12, -5, -6, 50, 3], 4, 12.75), ([5], 1, 5)],
)
def test_max_average_subarray(nums, k, expected):
    solution = Solution()
    assert solution.findMaxAverage(nums, k) == expected
