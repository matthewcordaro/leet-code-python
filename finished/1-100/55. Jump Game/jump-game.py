import unittest


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def canJump(self, nums: list[int]) -> bool:
        nums[-1] = 1
        for n in reversed(nums[:-1]):
            # Greedy: reset if enough, otherwise another needed
            nums[-1] = 1 if n >= nums[-1] else nums[-1] + 1
        return nums[-1] == 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.canJump([2, 3, 1, 1, 4]))
        self.assertTrue(self.sol.canJump([2]))

        self.assertFalse(self.sol.canJump([3, 2, 1, 0, 4]))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
