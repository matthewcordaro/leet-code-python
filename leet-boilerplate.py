import unittest
from typing import List


# O()
class Solution:
  def someFunction(self, variable: List[int]):
    pass


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(self.sol.someFunction([]), 0)


def main():
    unittest.main()


if __name__ == '__main__':
  main()
