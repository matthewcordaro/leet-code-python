from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def singleNumber(self, nums: [int]) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, self.sol.singleNumber([2, 2, 1]))
        self.assertEqual(-1, self.sol.singleNumber(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 12, 13, 13, 14, 14, 11, 11, 15, 16, 17, 16,
             15, ]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
