import pytest
from src.stack.decode_string.solution import (
    Solution,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ],
)
def test_decode_string(s, expected):
    solution = Solution()
    assert solution.decodeString(s) == expected
