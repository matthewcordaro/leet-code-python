from unittest import TestCase


def thereExistsAFreshOrange(grid: list[list[int]]) -> bool:
    for row in grid:
        for cell in row:
            if cell == 1:
                return True
    return False


def freshExistsHere(y, x, grid: list[list[int]]) -> bool:
    return 0 <= y <= len(grid) - 1 and \
        0 <= x <= len(grid[0]) - 1 and \
        grid[y][x] == 1


# if no update, returns None
def updateAdjacent(y: int, x: int, grid: list[list[int]]) -> list[list[int]] | None:
    updated = False
    if freshExistsHere(y - 1, x, grid):
        grid[y - 1][x] = 2
        updated = True
    if freshExistsHere(y + 1, x, grid):
        grid[y + 1][x] = 2
        updated = True
    if freshExistsHere(y, x - 1, grid):
        grid[y][x - 1] = 2
        updated = True
    if freshExistsHere(y, x + 1, grid):
        grid[y][x + 1] = 2
        updated = True

    if not updated:
        return None
    return grid


# if no update, returns None
def turnOranges(grid: list[list[int]]) -> list[list[int]] | None:
    rotting_locations: list[(int, int)] = []
    for y in range(len(grid)):  # rows
        for x in range(len(grid[y])):
            if grid[y][x] == 2:
                rotting_locations.append((y, x))

    updated = False
    for (y, x) in rotting_locations:
        new_grid = updateAdjacent(y, x, grid)
        if new_grid is not None:
            updated = True
            grid = new_grid

    if not updated:
        return None
    return grid


class Solution:
    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def orangesRotting(self, grid: list[list[int]]) -> int:
        turns: int = 0
        # if any fresh oranges, make attempt
        while thereExistsAFreshOrange(grid):
            new_grid = turnOranges(grid)
            # if we can't update anymore
            if new_grid is None:
                # but there still is a fresh one
                if thereExistsAFreshOrange(grid):
                    return -1
                break  # we are done
            grid = new_grid
            turns += 1
        return turns


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(4, self.sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
        self.assertEqual(-1, self.sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
        self.assertEqual(0, self.sol.orangesRotting([[0, 2]]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
