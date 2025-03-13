from unittest import TestCase


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        left_low = 0
        for right_index in range(1, len(prices)):
            if prices[right_index] < prices[left_low]:
                # set new lowest
                left_low = right_index
            else:
                # compare range price to max
                max_profit = max(max_profit, prices[right_index] - prices[left_low])

        return max_profit


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxProfit(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3, 4, 5, 4, 3, 2, 1]), 4)
        self.assertEqual(self.sol.maxProfit([4, 5, 4, 3, 2, 1, 2, 3, 4]), 3)
        self.assertEqual(self.sol.maxProfit([3, 4, 5, 4, 3, 2, 1, 2]), 2)
        self.assertEqual(self.sol.maxProfit([5, 4, 3, 2, 1, 1, 2, 3, 4]), 3)
        self.assertEqual(self.sol.maxProfit([5, 4, 3, 2, 1]), 0)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
