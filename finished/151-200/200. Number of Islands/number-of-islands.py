from unittest import TestCase


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        num_islands = 0
        width, height = len(grid[0]), len(grid)
        y = 0
        while y < height:
            x = 0
            while x < width:
                if int(grid[y][x]) == 1:
                    num_islands += 1
                    grid = self.floodFillID(grid, x, y, str(num_islands + 1))
                x += 1
            y += 1
        return num_islands

    def floodFillID(self, grid: [[str]], x: int, y: int, ff_id: str):
        if int(grid[y][x]) != 1:
            return grid
        grid[y][x] = ff_id
        width, height = len(grid[0]), len(grid)
        for xr in range(x + 1, width):  # go right
            if int(grid[y][xr]) != 1:
                break  # until
            grid = self.floodFillID(grid, xr, y, ff_id)
        for xl in range(x - 1, -1, -1):  # go left
            if int(grid[y][xl]) != 1:
                break  # until
            grid = self.floodFillID(grid, xl, y, ff_id)
        for yd in range(y + 1, height):  # go down
            if int(grid[yd][x]) != 1:
                break  # until
            grid = self.floodFillID(grid, x, yd, ff_id)
        for yu in range(y - 1, -1, -1):  # go up
            if int(grid[yu][x]) != 1:
                break  # until
            grid = self.floodFillID(grid, x, yu, ff_id)
        return grid


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, self.sol.numIslands([["1", "1", "1", "1", "0"],
                                                 ["1", "1", "0", "1", "0"],
                                                 ["1", "1", "0", "0", "0"],
                                                 ["0", "0", "0", "0", "0"]]))
        self.assertEqual(1, self.sol.numIslands([["1", "1", "1"],
                                                 ["0", "1", "0"],
                                                 ["1", "1", "1"]]
                                                ))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
