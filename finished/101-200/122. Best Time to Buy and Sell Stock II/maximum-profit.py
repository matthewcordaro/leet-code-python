import unittest
from typing import List


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    # min = 0 max = 10**4
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for date in range(1, len(prices)):
            if prices[date - 1] < prices[date]:
                total += prices[date] - prices[date - 1]  # take profit
        return total


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(7, self.sol.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, self.sol.maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(0, self.sol.maxProfit([7, 6, 4, 3, 1]))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
