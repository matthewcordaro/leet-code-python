from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def rob(self, nums: list[int]) -> int:
        # Base Cases
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        # Track the last two house's max
        two_ago = nums[0]
        one_ago = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # take this house or skip
            current = max(nums[i] + two_ago, one_ago)
            # setup for next house
            two_ago, one_ago = one_ago, current
        return one_ago  # end of the block


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
