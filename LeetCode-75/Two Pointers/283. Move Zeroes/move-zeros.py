from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1
        """
        i, j = 0, 1
        while j < len(nums):
            if i >= j or nums[j] == 0:
                j += 1
                continue
            if nums[i] != 0:
                i += 1
                continue
            # now i is 0 and j isn't 0
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j + 1
        return


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
        self.sol.moveZeroes(nums)
        self.assertListEqual([4, 2, 4, 3, 5, 1, 0, 0, 0, 0], nums)
        nums = [2, 1]
        self.sol.moveZeroes(nums)
        self.assertListEqual([2, 1], nums)
        nums = [1, 0, 1]
        self.sol.moveZeroes(nums)
        self.assertListEqual([1, 1, 0], nums)
        nums = [0, 1, 0, 3, 12]
        self.sol.moveZeroes(nums)
        self.assertListEqual([1, 3, 12, 0, 0], nums)
        nums = [0]
        self.sol.moveZeroes(nums)
        self.assertListEqual([0], nums)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
