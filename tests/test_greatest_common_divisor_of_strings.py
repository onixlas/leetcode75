import pytest
from array_string.greatest_common_divisor_of_strings.solution import Solution

@pytest.mark.parametrize("str1, str2, expected", [
    ("ABCABC", "ABC", "ABC"),
    ("ABABAB", "ABAB", "AB"),
    ("LEET", "CODE", "")
])
def test_merge_alternately(str1, str2, expected):
    solution = Solution()
    assert solution.gcdOfStrings(str1, str2) == expected