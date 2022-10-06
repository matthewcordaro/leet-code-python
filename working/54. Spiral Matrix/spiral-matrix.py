import unittest
from typing import List


class Direction:
  RIGHT = 0
  LEFT = 1
  UP = 2
  DOWN = 3


# O()
class Solution:

  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if matrix is []:
      return []

    width, height = len(matrix[0]), len(matrix)
    visited = [[False for _ in range(width)] for _ in range(height)]
    size = width * height
    l: List[int] = []

    # Where to start
    y, x = (0, 0)
    direction = Direction.RIGHT  # start going right

    # Main Loop
    while len(l) < size:
      visited[y][x] = True
      l.append(matrix[y][x])
      if direction is Direction.RIGHT:
        x += 1
        if x is not width and not visited[y][x]: continue
        x, y = x-1, y+1
        direction = Direction.DOWN
      elif direction is Direction.DOWN:
        y += 1
        if y is not height and not visited[y][x]: continue
        x, y = x-1, y-1
        direction = Direction.LEFT
      elif direction is Direction.LEFT:
        x -= 1
        if x is not -1 and not visited[y][x]: continue
        x, y = x+1, y-1
        direction = Direction.UP
      elif direction is Direction.UP:
        y -= 1
        if y is not -1 and not visited[y][x]: continue
        x, y = x+1, y+1
        direction = Direction.RIGHT
    return l


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], self.sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
