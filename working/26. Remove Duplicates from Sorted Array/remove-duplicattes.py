import unittest
from typing import List


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def removeDuplicates(self, nums: List[int]) -> int:
    pass


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    # Documentation on Python site wrong.
    # Expected: 1st argument
    # Actual:   2nd argument (items to test)
    self.assertEqual([0,1,2,3,4,None,None,None,None,None], self.sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def main():
    unittest.main()


if __name__ == '__main__':
  main()
