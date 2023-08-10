from _heapq import heappush, heappop
from unittest import TestCase


# O()
class MedianFinder:
    # Size of max_heap should always be == or +1 than min_heap

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num > self.max_heap[0]:
            heappush(self.max_heap, num)
            if len(self.max_heap) - len(self.min_heap) == 2:
                heappush(self.min_heap, -heappop(self.max_heap))
        else:
            heappush(self.min_heap, -num)
            if len(self.min_heap) - len(self.max_heap) == 1:
                heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] - self.min_heap[0]) / 2
        return self.max_heap[0]

    def balance(self) -> None:
        # Assumes all items in min are smaller than all items in max
        while abs(len(self.max_heap) - len(self.min_heap)) >= 2:
            # Move one from larger heap to the other
            heaps = [self.min_heap, self.max_heap]
            heaps.sort(key=len)
            heappush(heaps[0], -heappop(heaps[1]))


class TestSolution(TestCase):
    def setUp(self):
        self.mf = MedianFinder()

    def test_solution(self):
        mf = self.mf
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(1.5, mf.findMedian())
        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
