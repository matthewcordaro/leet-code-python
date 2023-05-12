import unittest
from typing import List


# O()
class Solution:
  def shuffle(self, nums: List[int], n: int) -> List[int]:
    result = [0] * (2 * n)
    for i in range(n):
      print(i)
      result[2 * i] = nums[i]
      result[2 * i + 1] = nums[n + i]
    return result


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual([1, 4, 2, 3, 3, 2, 4, 1], self.sol.shuffle([1, 2, 3, 4, 4, 3, 2, 1], n=4))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
