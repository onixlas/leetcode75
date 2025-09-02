from collections import deque


class RecentCounter:
    def __init__(self):
        self.deque = deque([])
        self._INTERVAL = 3000

    def ping(self, t: int) -> int:
        previous = t - self._INTERVAL

        while self.deque and self.deque[0] < previous:
            self.deque.popleft()

        self.deque.append(t)

        return len(self.deque)
