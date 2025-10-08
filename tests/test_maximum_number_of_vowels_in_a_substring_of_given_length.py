import pytest
from src.sliding_window.maximum_number_of_vowels_in_a_substring_of_given_length.solution import (
    Solution,
)


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
    ],
)
def test_max_vowels(s, k, expected):
    solution = Solution()
    assert solution.maxVowels(s, k) == expected
