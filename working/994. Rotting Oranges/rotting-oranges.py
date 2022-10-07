import unittest
from typing import List


def thereExistsAFreshOrange(grid: List[List[int]]) -> bool:
  for row in grid:
    for cell in row:
      if cell == 1:
        return True
  return False


def freshExistsHere(y, x, grid: List[List[int]]) -> bool:
  return 0 <= y <= len(grid) - 1 and \
         0 <= x <= len(grid[0]) - 1 and \
         grid[y][x] == 1


def getListOfCellType(t: int, grid: List[List[int]]) -> List[(int, int)]:
  l: [(int, int)] = []
  for y in range(len(grid)):  # rows
    for x in range(len(grid[y])):
      if grid[y, x] == t:
        l.append((y, x))
  return l


# if no update, returns None
def updateAdjacent(y: int, x: int, grid: List[List[int]]) -> List[List[int]]:
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
def turnOranges(grid: List[List[int]]) -> List[List[int]]:
  rotting_locations: List[(int, int)] = []
  for y in range(len(grid)):  # rows
    for x in range(len(grid[y])):
      if grid[y][x] == 2:
        rotting_locations.append((y, x))
  # ToDo There is a better way when we maintain this and don't calculate it all the time.
  updated = False
  for (y, x) in rotting_locations:
    new_grid = updateAdjacent(y, x, grid)
    if new_grid is not None:
      updated = True
      grid = new_grid

  if not updated:
    return None
  return grid


def rot(grid: List[List[int]]) -> int:
  # get initial rot
  rotted_locations: set[int, int] = set()
  for y in range(len(grid)):  # rows
    for x in range(len(grid[y])):
      if grid[y][x] == 2:
        rotted_locations.add(y, x)
  if len(rotted_locations) is 0:
    return 0

  turns = 0
  last_rot_locations = rotted_locations
  new_grid = grid
  while thereExistsAFreshOrange(grid):
    # next rot
    for lrl in last_rot_locations:
      new_locations = updateAdjacentList(*lrl, grid)
      if new_locations is not 0:
        new_grid = updateAdjacent(*lrl, new_grid)


    pass


def updateAdjacentList(y: int, x: int, grid: List[List[int]]) -> List[(int, int)]:
  l: [(int, int)] = []
  if freshExistsHere(y - 1, x, grid):
    l.append((y - 1, x))
  if freshExistsHere(y + 1, x, grid):
    l.append((y + 1, x))
  if freshExistsHere(y, x - 1, grid):
    l.append((y, x - 1))
  if freshExistsHere(y, x + 1, grid):
    l.append((y, x + 1))
  return l


class Solution:
  def __init__(self):
    pass

  def orangesRotting(self, grid: List[List[int]]) -> int:
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


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(4, self.sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    self.assertEqual(-1, self.sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    self.assertEqual(0, self.sol.orangesRotting([[0, 2]]))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
