from unittest import TestCase


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def increasingTriplet(self, nums: [int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        # array of smallest index to the left
        # array of largest index to the right
        # look for i < j < k
        left_smallest_num = nums[0]
        right_largest_nums = [-2 ** 31] * length
        right_largest_nums[len(nums) - 1] = nums[-1]
        # calc largest
        for i, num in reversed(list(enumerate(nums[:-1]))):
            right_largest_nums[i] = max(right_largest_nums[i + 1], num)
        # calc smallest and check
        for i, num in enumerate(nums[1:-1]):
            left_smallest_num = min(left_smallest_num, num)
            if left_smallest_num < num < right_largest_nums[i + 1]:
                return True
        return False

    # NOT A SOLUTION TO Increasing Triplet Subsequence
    # noinspection PyMethodMayBeStatic
    def increasingTripletSubarray(self, nums: [int]) -> bool:
        if len(nums) < 3:
            return False
        last_ok = nums[0] < nums[1]
        last_num = nums[1]
        for num in nums[2:]:
            if last_ok:
                if last_num < num:
                    return True
            last_ok = last_num < num
            last_num = num
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
