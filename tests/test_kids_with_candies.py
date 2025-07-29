import pytest
from array_string.kids_with_the_greatest_number_of_candies.solution import Solution

@pytest.mark.parametrize("candies, extraCandies, expected", [
    ([2, 3, 5, 1, 3], 3, [True, True, True, False, True] ),
    ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ([12, 1, 12], 10, [True, False, True])
])
def test_merge_alternately(candies, extraCandies, expected):
    solution = Solution()
    assert solution.kidsWithCandies(candies, extraCandies) == expected