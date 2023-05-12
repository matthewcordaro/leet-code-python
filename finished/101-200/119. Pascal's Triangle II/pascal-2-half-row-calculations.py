import unittest
from typing import List


# O()
class Solution:
  def __init__(self):
    self.pascal_triangle = [[1], [1, 1]]

  def getRow(self, rowIndex: int) -> List[int]:
    # Solution not stored? Keep building
    while rowIndex > len(self.pascal_triangle) - 1:
      bottom_row = self.pascal_triangle[-1]
      new_row = [1]  # Each row begins with a 1

      # Calculate & finish first half
      for i in range(1, int(len(bottom_row) / 2) + 1):
        new_row.append(bottom_row[i - 1] + bottom_row[i])
        i += 1

      # Copy first half to second
      # Note: Converting a float type to int type removes the decimal part.
      #   Odd length rows will be `n.5 -> n` ex: 2.5 -> 2
      #   So here the middle number will be skipped.
      for i in range(int((len(bottom_row) - 1) / 2), -1, -1):
        new_row.append(new_row[i])

      self.pascal_triangle.append(new_row)
    return self.pascal_triangle[rowIndex]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    # Documentation on Python site wrong.
    # Expected: 1st argument
    # Actual:   2nd argument (items to test)
    self.assertEqual([1], self.sol.getRow(0))
    self.assertEqual([1, 1], self.sol.getRow(1))
    self.assertEqual([1, 2, 1], self.sol.getRow(2))
    self.assertEqual([1, 3, 3, 1], self.sol.getRow(3))
    self.assertEqual([1, 4, 6, 4, 1], self.sol.getRow(4))
    self.assertEqual([1, 5, 10, 10, 5, 1], self.sol.getRow(5))
    self.assertEqual([1,
                      20,
                      190,
                      1140,
                      4845,
                      15504,
                      38760,
                      77520,
                      125970,
                      167960,
                      184756,
                      167960,
                      125970,
                      77520,
                      38760,
                      15504,
                      4845,
                      1140,
                      190,
                      20,
                      1],
                     self.sol.getRow(20))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
