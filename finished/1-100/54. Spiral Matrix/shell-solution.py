import unittest
from typing import List


# O(n+m)
# Each loop takes care of outermost shell of rectangle
class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if matrix is []:
      return []

    left, top, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1  # edges
    number_of_cells = len(matrix[0]) * len(matrix)
    solution: List[int] = []

    while len(solution) < number_of_cells:
      for x in range(left, right + 1):
        solution.append(matrix[top][x])
      top += 1
      for y in range(top, bottom + 1):
        solution.append(matrix[y][right])
      right -= 1
      if not len(solution) < number_of_cells: break  # for even row or cols
      for x in range(right, left - 1, -1):
        solution.append(matrix[bottom][x])
      bottom -= 1
      for y in range(bottom, top - 1, -1):
        solution.append(matrix[y][left])
      left += 1

    return solution


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(self.sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                     [1, 2, 3, 6, 9, 8, 7, 4, 5])
    self.assertEqual(self.sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
                     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])


def main():
  unittest.main()


if __name__ == '__main__':
  main()
