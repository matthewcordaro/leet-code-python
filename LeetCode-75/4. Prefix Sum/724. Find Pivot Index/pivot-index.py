from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, i, right_sum = 0, 0, sum(nums[1:])
        while i < len(nums) - 1:
            if left_sum == right_sum:
                return i
            # Order matters below
            left_sum += nums[i]
            i += 1
            right_sum -= nums[i]
        return i if left_sum == right_sum else -1


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
        self.assertEqual(-1, self.sol.pivotIndex(nums=[1, 2, 3]))
        self.assertEqual(0, self.sol.pivotIndex(nums=[2, 1, -1]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
