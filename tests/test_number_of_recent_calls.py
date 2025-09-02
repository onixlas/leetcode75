import pytest
from src.queue.number_of_recent_calls.solution import RecentCounter


@pytest.mark.parametrize(
    "calls, args, expected",
    [
        (
            ["RecentCounter", "ping", "ping", "ping", "ping"],
            [[], [1], [100], [3001], [3002]],
            [None, 1, 2, 3, 3],
        ),
    ],
)
def test_recent_counter(calls, args, expected):
    obj = None
    results = []

    for call, arg, exp in zip(calls, args, expected):
        if call == "RecentCounter":
            obj = RecentCounter()
            results.append(None)
        else:
            method = getattr(obj, call)
            res = method(*arg)
            results.append(res)

    assert results == expected
