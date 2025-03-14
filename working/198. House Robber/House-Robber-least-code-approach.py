from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def rob(self, nums: list[int]) -> int:
        prev_home, this_home = 0, 0  # start with blank houses to simplify logic
        for money in nums:
            prev_home, this_home = this_home, max(prev_home + money, this_home)
        return this_home  # last house on the block


# noinspection SpellCheckingInspection
class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # LeetCode's first example
        self.assertEqual(self.sol.rob([1, 2, 3, 1]), 4)

    def test_example2(self):
        # LeetCode's second example
        self.assertEqual(self.sol.rob([2, 7, 9, 3, 1]), 12)

    def test_example3(self):
        # LeetCode's failed example
        self.assertEqual(self.sol.rob([1,1,1]), 2)

    def test_empty_house(self):
        self.assertEqual(self.sol.rob([]), 0)

    def test_single_house(self):
        self.assertEqual(self.sol.rob([1]), 1)

    def test_two_houses(self):
        self.assertEqual(self.sol.rob([1, 2]), 2)

    def test_longer_sequence(self):
        self.assertEqual(self.sol.rob([2, 1, 1, 2]), 4)

    def test_all_same_values(self):
        self.assertEqual(self.sol.rob([5, 5, 5, 5]), 10)

    def test_increasing_sequence(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 4, 5]), 9)

    def test_decreasing_sequence(self):
        self.assertEqual(self.sol.rob([5, 4, 3, 2, 1]), 9)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
