import pytest
from array_string.merge_strings_alternately.solution import Solution

@pytest.mark.parametrize("word1, word2, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd")
])
def test_merge_alternately(word1, word2, expected):
    solution = Solution()
    assert solution.mergeAlternately(word1, word2) == expected