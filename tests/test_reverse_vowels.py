import pytest
from src.array_string.reverse_vowels_of_a_string.solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [("IceCreAm", "AceCreIm"), ("leetcode", "leotcede"), (" ", " ")],
)
def test_reverse_vowels(s, expected):
    solution = Solution()
    assert solution.reverseVowels(s) == expected
