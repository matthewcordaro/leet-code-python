from collections import Counter
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_counts = Counter(map(tuple, grid))  # map, hash, keep total
        column_counts = Counter(zip(*grid))  # transpose, hash, keep total
        return sum(column_counts[r] * row_counts[r] for r in row_counts)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1,
                         self.sol.equalPairs(
                             grid=[[3, 2, 1],
                                   [1, 7, 6],
                                   [2, 7, 7]]))
        self.assertEqual(3,
                         self.sol.equalPairs(
                             grid=[[3, 1, 2, 2],
                                   [1, 4, 4, 5],
                                   [2, 4, 2, 2],
                                   [2, 4, 2, 2]]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
