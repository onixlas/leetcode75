import pytest
from src.stack.removing_stars_from_a_string.solution import (
    Solution,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ],
)
def test_remove_stars(s, expected):
    solution = Solution()
    assert solution.removeStars(s) == expected
