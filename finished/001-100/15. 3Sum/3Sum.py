from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solution = []
        nums_len = len(nums)
        for i in range(0, nums_len - 2):
            x = nums[i]
            for j in range(i + 1, nums_len - 1):
                y = nums[j]
                for k in range(j + 1, nums_len):
                    z = nums[k]
                    if x + y + z == 0:
                        new_item = [x, y, z]
                        new_item.sort()
                        if new_item not in solution:
                            solution.append(new_item)
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        # self.assertEqual([],
        #                  self.sol.threeSum([0, 1, 1]))
        # self.assertEqual([[-1, -1, 2], [-1, 0, 1]],
        #                  self.sol.threeSum([-1, 0, 1, 2, -1, -4]))
        self.assertEqual([[0, 0, 0]],
                         self.sol.threeSum([0, 0, 0]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
