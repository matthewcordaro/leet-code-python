from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        pass


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(True,
                         self.sol.searchMatrix(matrix=[[1, 3, 5, 7],
                                                       [10, 11, 16, 20],
                                                       [23, 30, 34, 60]],
                                               target=3))
        self.assertEqual(True,
                         self.sol.searchMatrix(matrix=[[1, 3, 5, 7],
                                                       [10, 11, 16, 20],
                                                       [23, 30, 34, 60]],
                                               target=13))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
