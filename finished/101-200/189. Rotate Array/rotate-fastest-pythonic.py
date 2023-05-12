import unittest
from typing import List


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def rotate(self, nums: List[int], k: int):
    k %= len(nums)  # avoid extra rotation
    nums [:] = nums[-k:] + nums[:-k]

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

def main():
    unittest.main()


if __name__ == '__main__':
  main()
