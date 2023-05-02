import unittest
from typing import List


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  # [3,3,5,0,0,3,1,4]: Buy 4, sell 6, buy 7 sell 8
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 1: return 0
    # This may not be necessary
    if len(prices) == 2: return prices[1] - prices[0] if prices[1] > prices[0] else 0

    peak_and_valley_days = [0]

    for i in range(1, len(prices)-1 ):
      if:   # local peak
      elif:  # local valley
      else:  # steady

    if prices[-2] > prices[-1]:
      lmin.append(prices[-1])
    else:
      lmax.append(prices[-1])


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(6, self.sol.maxProfit([3,3,5,0,0,3,1,4]))
    self.assertEqual(4, self.sol.maxProfit([1,2,3,4,5]))
    self.assertEqual(0, self.sol.maxProfit([7,6,4,3,1]))


def main():
    unittest.main()


if __name__ == '__main__':
  main()
