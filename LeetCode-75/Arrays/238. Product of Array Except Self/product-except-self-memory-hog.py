from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_multiply = [1] * len(nums)
        right_multiply = [1] * len(nums)
        for i in range(1, len(nums)):
            left_multiply[i] = nums[i-1] * left_multiply[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_multiply[i] = nums[i+1] * right_multiply[i+1]
        return [l * r for (l, r) in zip(left_multiply, right_multiply)]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertListEqual([24, 12, 8, 6], self.sol.productExceptSelf(nums=[1, 2, 3, 4]))
        self.assertListEqual([0, 0, 9, 0, 0], self.sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
