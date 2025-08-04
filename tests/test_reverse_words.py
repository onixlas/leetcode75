import pytest
from src.array_string.reverse_words_in_a_string.solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
    ],
)
def test_reverse_words(s, expected):
    solution = Solution()
    assert solution.reverseWords(s) == expected
