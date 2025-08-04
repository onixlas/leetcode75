import pytest
from src.two_pointers.move_zeroes.solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
    ],
)
def test_move_zeroes(nums, expected):
    Solution().moveZeroes(nums)
    assert nums == expected
