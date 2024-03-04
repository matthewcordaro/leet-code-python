from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def longestOnes(self, nums: list[int], k: int) -> int:
        solution = 0
        li = 0
        for ri in range(len(nums)):
            if nums[ri] == 1:  # simply take the 1
                solution = max(solution, ri - li + 1)
            else:  # 0 case
                k -= 1  # take a zero
                if k >= 0:  # if we didn't take too much
                    solution = max(solution, ri - li + 1)
                else:  # we took too many
                    while nums[li] != 0:  # move forward to find a zero
                        li += 1
                    # remove the zero to free for another one
                    li += 1
                    k += 1
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(6, self.sol.longestOnes(
            nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
            k=2))
        self.assertEqual(10, self.sol.longestOnes(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            k=3))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
