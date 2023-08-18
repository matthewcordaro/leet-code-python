import unittest
from typing import List
from bisect import *


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        for i in range(len(numbers)):
            j = bisect_left(numbers, target - numbers[i], lo=i + 1, hi=j)
            if target - numbers[i] - numbers[j] == 0 and i != j:
                return [i + 1, j + 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_twoSum(self):
        self.assertEqual(self.sol.twoSum([1, 2, 3, 4, 5, 6], 4), [1, 3])
        self.assertEqual(self.sol.twoSum([0, 0, 3, 4], 0), [1, 2])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
