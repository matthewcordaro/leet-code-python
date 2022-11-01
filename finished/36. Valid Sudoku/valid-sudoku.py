import unittest
from typing import List, Iterable
import numpy as np


# O()
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    board = np.array(board)
    for line in board:  # Rows
      if not self.isValidSudokuPart(line): return False
    for m in range(3, 10, 3):  # Boxes
      for n in range(3, 10, 3):
        if not self.isValidSudokuPart(np.nditer(board[m - 3:m, n - 3:n])): return False
    board = board.T
    for line in board:  # Columns
      if not self.isValidSudokuPart(line): return False
    return True

  @staticmethod
  def isValidSudokuPart(i: Iterable[str]) -> bool:
    is_found = [False for _ in range(9)]
    for val in i:
      if val == '.': continue
      val = int(val) - 1
      if is_found[val]: return False
      is_found[val] = True
    return True


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol = True
    self.assertEqual(sol, self.sol.isValidSudoku(board))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
