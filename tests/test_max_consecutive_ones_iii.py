import pytest
from src.sliding_window.max_consecutive_ones_iii.solution import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ],
)
def test_longest_ones(nums, k, expected):
    solution = Solution()
    assert solution.longestOnes(nums, k) == expected
