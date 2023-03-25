import unittest
from typing import List


# O(n)
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    s = set()
    for n in nums:
      if n in s: return True
      s.add(n)
    return False


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_containsDuplicate(self):
    self.assertFalse(self.sol.containsDuplicate([1, 2, 3, 4, 5, 6]))
    self.assertTrue(self.sol.containsDuplicate([1, 2, 3, 4, 5, 6, 6]))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
