from unittest import TestCase


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return True if there exists a triple of indices (i, j, k) such that i < j < k and
        nums[i] < nums[j] < nums[k]. If no such indices exists, return False.
        Must be O(n) complexity, O(1) space.
        1 <= len(nums) <= 500,000
        -2^31 <= nums[i] <= 2^31 - 1
        :param nums:
        :return:
        """
        # make a min array starting at max number
        min_int = 2**31 - 1
        max_int = -2**31
        min_prev = []
        for num in nums:
            min_prev.append(min_int)
            min_int = min(num, min_int)
        for idx, num in reversed(list(enumerate(nums))):
            if min_prev[idx] < nums[idx] < max_int:
                return True
            max_int = max(num, max_int)
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
