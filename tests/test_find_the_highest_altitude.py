import pytest
from src.prefix_sum.find_the_highest_altitude.solution import Solution


@pytest.mark.parametrize(
    "gain, expected",
    [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    ],
)
def test_largest_altitude(gain, expected):
    solution = Solution()
    assert solution.largestAltitude(gain) == expected
