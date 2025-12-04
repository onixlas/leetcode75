import pytest
from src.stack.asteroid_collision.solution import (
    Solution,
)


@pytest.mark.parametrize(
    "asteroids, expected",
    [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([3, 5, -6, 2, -1, 4], [-6, 2, 4]),
    ],
)
def test_asteroid_collision(asteroids, expected):
    solution = Solution()
    assert solution.asteroidCollision(asteroids) == expected
