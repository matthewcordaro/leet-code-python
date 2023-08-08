from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # Action: Rain flows to 4 sides of cell
        # Action: The Ocean can take an infinite amount in from the edge cells
        # Constraint: Flow only happens from larger cells to smaller cells
        pass


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            self.sol.pacificAtlantic(
                heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5],
                         [5, 1, 1, 2, 4]]))

        self.assertEqual([[0, 0]], self.sol.pacificAtlantic(heights=[[1]]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
