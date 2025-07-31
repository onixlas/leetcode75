import pytest
from array_string.can_place_flowers.solution import Solution

@pytest.mark.parametrize("flowerbed, n, expected", [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
    ([1,0,1,0,1,0,1], 1, False),
    ([1, 0, 0, 0, 1, 0, 0], 2, True),
    ([0], 1, True),
    ([1,0,1,0,1,0,1], 0, True)
])
def test_merge_alternately(flowerbed, n, expected):
    solution = Solution()
    assert solution.canPlaceFlowers(flowerbed, n) == expected