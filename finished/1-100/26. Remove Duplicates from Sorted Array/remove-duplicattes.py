import unittest
from typing import List


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def removeDuplicates(self, nums: List[int]) -> int:
    left = 0
    for right in range(len(nums)):
      if nums[left] != nums[right]:
        left += 1  # new number, move over
        nums[left] = nums[right]
    return left + 1



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(5, self.sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def main():
    unittest.main()


if __name__ == '__main__':
  main()
