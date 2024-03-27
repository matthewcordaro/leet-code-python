from collections import deque
from unittest import TestCase


# O()
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    # noinspection PyMethodMayBeStatic
    def ping(self, t: int) -> int:
        self.requests.append(t)  # Every call to ping, larger value of t than the previous call
        t -= 3000
        while self.requests[0] < t:
            self.requests.popleft()  # Discard old values
        return len(self.requests)


class TestSolution(TestCase):
    def setUp(self):
        self.recentCounter = RecentCounter()

    def test_solution(self):
        self.assertEqual(1, self.recentCounter.ping(1))
        self.assertEqual(2, self.recentCounter.ping(100))
        self.assertEqual(3, self.recentCounter.ping(3001))
        self.assertEqual(3, self.recentCounter.ping(3002))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
