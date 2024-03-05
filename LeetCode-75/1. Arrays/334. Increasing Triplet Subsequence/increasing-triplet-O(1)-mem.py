from unittest import TestCase


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def increasingTriplet(self, nums: list[int]) -> bool:
        smol = smol_2 = 2**31 - 1
        for num in nums:
            if num <= smol:  # smallest number so far.  LE operation is important for else cases.
                smol = num
            elif num <= smol_2:  # 2nd smallest number so far. After smol in the array by definition.
                smol_2 = num
            else:  # 3rd smallest, means we found our solution: smol < smol_2 < num
                return True
        return False


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.increasingTriplet(nums=[1, 2, 3, 4, 5]))
        self.assertTrue(self.sol.increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))

        # 10, 12, 13
        self.assertTrue(self.sol.increasingTriplet(nums=[20, 100, 10, 12, 5, 13]))
        self.assertFalse(self.sol.increasingTriplet(nums=[5, 4, 3, 2, 1]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
