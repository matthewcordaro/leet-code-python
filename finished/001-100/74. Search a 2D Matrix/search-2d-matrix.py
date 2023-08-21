from bisect import bisect_left, bisect_right
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False
        # Find the row the target will fit in; at the row BEFORE the right bisection
        row = bisect_right([r[0] for r in matrix], target) - 1
        # Find the column the target will fit in; at the col of the left bisection
        col = bisect_left(matrix[row], target)
        # Solution is at row, col. Just make sure col is valid
        return col < len(matrix[0]) and matrix[row][col] == target


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.searchMatrix(matrix=[[1, 3, 5, 7],
                                                      [10, 11, 16, 20],
                                                      [23, 30, 34, 60]],
                                              target=3))
        self.assertTrue(self.sol.searchMatrix(matrix=[[1, 3]],
                                              target=1))

        self.assertFalse(self.sol.searchMatrix(matrix=[[1, 3, 5, 7],
                                                       [10, 11, 16, 20],
                                                       [23, 30, 34, 60]],
                                               target=13))
        self.assertFalse(self.sol.searchMatrix(matrix=[[1, 3, 5, 7],
                                                       [10, 11, 16, 20],
                                                       [23, 30, 34, 60]],
                                               target=0))
        self.assertFalse(self.sol.searchMatrix(matrix=[[1, 3, 5, 7],
                                                       [10, 11, 16, 20],
                                                       [23, 30, 34, 60]],
                                               target=21))
        self.assertFalse(self.sol.searchMatrix(matrix=[[1, 3, 5, 7],
                                                       [10, 11, 16, 20],
                                                       [23, 30, 34, 60]],
                                               target=61))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
