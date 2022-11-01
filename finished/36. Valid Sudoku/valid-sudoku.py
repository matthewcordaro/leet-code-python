import array
import unittest
from typing import List

import numpy as np


# O()
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Plan:
    # Validate the 9 rows iterating in helper function
    # transpose
    # validate 9 rows again
    # slice and check 9 boxes in helper function that takes 3x3

    b = np.array(board)
    for line in b:
      if not self.isValidLine(line): return False

    # Could clean this up..
    if not self.isValidBox(b[:3, :3]): return False
    if not self.isValidBox(b[:3, 3:6]): return False
    if not self.isValidBox(b[:3, 6:9]): return False
    if not self.isValidBox(b[3:6, :3]): return False
    if not self.isValidBox(b[3:6, 3:6]): return False
    if not self.isValidBox(b[3:6, 6:9]): return False
    if not self.isValidBox(b[6:9, :3]): return False
    if not self.isValidBox(b[6:9, 3:6]): return False
    if not self.isValidBox(b[6:9, 6:9]): return False

    b = b.T
    for line in b:
      if not self.isValidLine(line): return False
    return True

  @staticmethod
  def isValidLine(line: array.ArrayType) -> bool:
    # validate 9 normally, but assume correct for now
    is_found = [False for _ in range(9)]
    for val in line:
      if val == '.': continue
      val = int(val) - 1
      if is_found[val]: return False  # collision
      is_found[val] = True
    return True

  @staticmethod
  def isValidBox(box: array.ArrayType) -> bool:
    # validate 3x3 normally, but assume correct for now
    is_found = [False for _ in range(9)]
    for row in box:
      for val in row:
        if val == '.': continue
        val = int(val) - 1
        if is_found[val]: return False  # collision
        is_found[val] = True
    return True


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol = True
    self.assertEqual(sol, self.sol.isValidSudoku(board))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
