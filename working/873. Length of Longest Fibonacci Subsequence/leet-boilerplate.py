import unittest
from typing import List


# O()
class Solution:
  def __init__(self):
    self.solution = []

  def lenLongestFibSubseq(self, arr: List[int]) -> int:
    pass


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    # Documentation on Python site wrong.
    # Expected: 1st argument
    # Actual:   2nd argument (items to test)
    self.assertEqual(5, self.sol.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
    self.assertEqual(3, self.sol.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
