from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def a_neighbor_is_rotten(self, row:int, col:int, grid:list[list[int]]) -> bool:
        # Returns True if a direct neighbor (4 sides) is rotten, otherwise False
        # Left, Right, Down, Up Respectively
        return (col > 0 and grid[row][col-1] == 2) or \
                (col + 1 < len(grid[0]) and grid[row][col + 1] == 2) or \
                (row + 1 < len(grid) and grid[row + 1][col] == 2) or \
                (row > 0 and grid[row-1][col] == 2)

    # noinspection PyMethodMayBeStatic
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Make a list of all the fresh oranges
        fresh_oranges = []
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1: fresh_oranges.append((r, c))
        # Edge Case
        if len(fresh_oranges) == 0:  return 0
        # keep looping all fresh until rotten or stuck
        solution = 0
        newly_rotten_oranges = ["-"]  # Needs something to pass first loop
        while len(newly_rotten_oranges) > 0 and len(fresh_oranges) > 0:
            solution += 1
            newly_rotten_oranges = []
            still_fresh_oranges = []
            # check neighbors for rotten
            while fresh_oranges:
                row, col = fresh_oranges.pop()
                if self.a_neighbor_is_rotten(row, col, grid):
                    newly_rotten_oranges.append((row, col))
                else:
                    still_fresh_oranges.append((row, col))
            # update for next iteration
            fresh_oranges = still_fresh_oranges
            for row, col in newly_rotten_oranges:
                grid[row][col] = 2

        return -1 if len(fresh_oranges) > 0 else solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_a_neighbor_is_rotten(self):
        self.assertTrue(self.sol.a_neighbor_is_rotten(0, 0, grid = [[0,2],[0,0]]))
        self.assertTrue(self.sol.a_neighbor_is_rotten(0, 0, grid = [[0,0],[2,0]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(0, 0, grid = [[0,0],[0,2]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(0, 0, grid = [[0,0],[0,0]]))

        self.assertTrue(self.sol.a_neighbor_is_rotten(0, 1, grid = [[2,0],[0,0]]))
        self.assertTrue(self.sol.a_neighbor_is_rotten(0, 1, grid = [[0,0],[0,2]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(0, 1, grid = [[0,0],[2,0]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(0, 1, grid = [[0,0],[0,0]]))

        self.assertTrue(self.sol.a_neighbor_is_rotten(1, 0, grid = [[2,0],[0,0]]))
        self.assertTrue(self.sol.a_neighbor_is_rotten(1, 0, grid = [[0,0],[0,2]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(1, 0, grid = [[0,2],[0,0]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(1, 0, grid = [[0,0],[0,0]]))

        self.assertTrue(self.sol.a_neighbor_is_rotten(1, 1, grid = [[0,2],[0,0]]))
        self.assertTrue(self.sol.a_neighbor_is_rotten(1, 1, grid = [[0,0],[2,0]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(1, 1, grid = [[2,0],[0,0]]))
        self.assertFalse(self.sol.a_neighbor_is_rotten(1, 1, grid = [[0,0],[0,0]]))

    def test_solution(self):
        self.assertEqual(4, self.sol.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
        self.assertEqual(-1, self.sol.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
        self.assertEqual(-1, self.sol.orangesRotting(grid = [[0,2]]))
        self.assertEqual(1, self.sol.orangesRotting(grid = [[1,2]]))

def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
