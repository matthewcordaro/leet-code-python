import unittest
from bisect import *
from typing import List, Callable


# O(m*n)
class IndexedInterval:
    def __init__(self, index: int, interval: List[int]):
        self.index = index
        self.low = interval[0]
        self.high = interval[1]
        self.width = interval[1] - interval[0] + 1

    def __lt__(self, other):
        return self.width > other.width

    def __eq__(self, other):
        return self.index == other.index

    def __str__(self):
        return "[" + str(self.low) + " - " + str(self.high) + "]"

    def __hash__(self):
        return int(self.index)

    def __repr__(self):
        return str(self.index) + ": " + str(self)


class Solution:
    # noinspection PyMethodMayBeStatic
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        solution = []
        l_sorted: list[IndexedInterval] = []  # interval low num index table
        h_sorted: list[IndexedInterval] = []  # interval high num index table
        l_key: Callable[[IndexedInterval], int] = lambda iv: iv.low
        h_key: Callable[[IndexedInterval], int] = lambda iv: iv.high
        for i in enumerate(intervals):
            ii = IndexedInterval(*i)
            insort(l_sorted, ii, key=l_key)
            insort(h_sorted, ii, key=h_key)
        for q in queries:
            bot = bisect_right(l_sorted, q, key=l_key)
            top = bisect_left(h_sorted, q, key=h_key)
            lows = set(l_sorted[:bot])
            highs = set(h_sorted[top:])
            intersection = lows.intersection(highs)
            min_len = -1
            if len(intersection) > 0:
                min_len = 10 ** 10
                for potential_solution in intersection:
                    min_len = min(min_len, potential_solution.width)
            solution.append(min_len)
        return solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([3, 3, 1, 4],
                         self.sol.minInterval(intervals=[[1, 4], [2, 4], [3, 6], [4, 4]],
                                              queries=[2, 3, 4, 5]))
        import test
        self.assertEqual([3, 3, 1, 4],
                         self.sol.minInterval(intervals=test.intervals, queries=test.queries))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
