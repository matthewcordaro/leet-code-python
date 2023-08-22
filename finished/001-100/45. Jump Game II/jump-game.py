from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        i = len(nums) - 1
        while i > 0:  # Working backwards from the end.
            for j in range(i):
                if i - j <= nums[j]:  # Greedy: take the earliest possible jump
                    i = j
                    jumps += 1
                    break
        return jumps


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(2, self.sol.jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, self.sol.jump([2, 3, 0, 1, 4]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
