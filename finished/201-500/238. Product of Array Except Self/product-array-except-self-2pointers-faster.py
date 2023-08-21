from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        sol = [1] * len_nums
        pre = post = 1
        # 2 ptrs: Update Sol, then update `pre` & `post`,
        for i in range(len_nums):
            j = len_nums - i - 1
            sol[i] *= pre
            sol[j] *= post
            pre *= nums[i]
            post *= nums[j]

        return sol


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([24, 12, 8, 6], self.sol.productExceptSelf([1, 2, 3, 4]))
        self.assertEqual([0, 0, 9, 0, 0], self.sol.productExceptSelf([-1, 1, 0, -3, 3]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
