import unittest
from typing import List


# O(n)
# global_maximum at `i` is the maximum of
#   global_max VS the sum of nums[i] and running total.
#   if < 0 reset to shift left starting of subarray window
class Solution:
    # noinspection PyMethodMayBeStatic
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        total = 0
        for num in nums:
            total += num
            global_max = max(global_max, total)
            if total < 0:
                total = 0
        return global_max


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(self.sol.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
