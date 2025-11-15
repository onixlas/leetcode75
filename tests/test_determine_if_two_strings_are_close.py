import pytest
from src.hashmap_set.determine_if_two_strings_are_close.solution import (
    Solution,
)


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("abc", "bca", True),
        ("a", "aa", False),
        ("cabbba", "abbccc", True),
    ],
)
def test_close_strings(word1, word2, expected):
    solution = Solution()
    assert solution.closeStrings(word1, word2) == expected
