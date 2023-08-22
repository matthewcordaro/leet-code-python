from unittest import TestCase
from bisect import bisect_left


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def twoSum(self, numbers: [int], target: int) -> [int]:
        j = len(numbers) - 1
        for i in range(len(numbers)):
            j = bisect_left(numbers, target - numbers[i], lo=i + 1, hi=j)
            if target - numbers[i] - numbers[j] == 0 and i != j:
                return [i + 1, j + 1]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_twoSum(self):
        self.assertEqual(self.sol.twoSum([1, 2, 3, 4, 5, 6], 4), [1, 3])
        self.assertEqual(self.sol.twoSum([0, 0, 3, 4], 0), [1, 2])


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
