from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        sol, prod = [], 1
        for num in nums:
            sol.append(prod)
            prod *= num
        prod = 1
        for i, num in reversed(list(enumerate(nums))):
            sol[i] *= prod
            prod *= num
        return sol


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
