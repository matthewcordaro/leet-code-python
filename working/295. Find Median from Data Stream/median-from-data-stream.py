import heapq
from unittest import TestCase


# O()
class MedianFinder:

    def __init__(self):
        self.median = True
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap if self.findMedian() > num else self.max_heap, num)
        # balance
        if len(self.min_heap) >= len(self.max_heap) + 2:
            pass
        elif len(self.max_heap) >= len(self.min_heap) + 2:
            pass

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:  # Average Both
            return (self.min_heap[0] + self.min_heap[0]) // 2


class TestSolution(TestCase):
    def setUp(self):
        self.sol = MedianFinder()

    def test_solution(self):
        # self.assertEqual(0, self.sol.someFunction())
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
