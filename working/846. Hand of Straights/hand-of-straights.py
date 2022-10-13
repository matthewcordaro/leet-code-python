import unittest
from typing import List


# O()
class Solution:
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    pass


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertTrue(self.sol.someFunction(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
