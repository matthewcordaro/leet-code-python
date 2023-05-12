import unittest
from typing import List


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def rotate(self, nums: List[int], k: int):
    if (n:=len(nums)) <= 1 or (k:=k%n) == 0: return nums
    def rev(l=0, r=(n-1)):  # reverse nums between left to right, inclusive
      while l < r:
        nums[l], nums[r] = nums[r], nums[l]  # swap
        l, r = l+1, r-1  # move inward
    rev()  # whole list
    rev(r=k-1)  # then the first k elements
    rev(l=k)  # then the rest
    return nums

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual([5,6,7,1,2,3,4], self.sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))


def main():
    unittest.main()


if __name__ == '__main__':
  main()
