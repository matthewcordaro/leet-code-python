from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def longestSubarray(self, nums: list[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        left = 0
        zeros = 0
        solution = 0
        max_zeros = 1
        for right in range(len(nums)):
            zeros += 1 if nums[right] == 0 else 0
            while zeros > max_zeros:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            solution = max(solution, right - left + 1 - zeros)
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.longestSubarray(nums=[1]))
        self.assertEqual(0, self.sol.longestSubarray(nums=[0]))
        self.assertEqual(0, self.sol.longestSubarray(nums=[0, 0]))
        self.assertEqual(1, self.sol.longestSubarray(nums=[0, 1]))
        self.assertEqual(1, self.sol.longestSubarray(nums=[1, 0]))
        self.assertEqual(1, self.sol.longestSubarray(nums=[1, 1]))
        self.assertEqual(1, self.sol.longestSubarray(nums=[1, 0, 0, 0, 1]))
        self.assertEqual(1, self.sol.longestSubarray(nums=[1, 0, 0, 1]))
        self.assertEqual(3, self.sol.longestSubarray(nums=[1, 1, 0, 1]))
        self.assertEqual(2, self.sol.longestSubarray(nums=[1, 1, 0, 0, 1]))
        self.assertEqual(2, self.sol.longestSubarray(nums=[0, 0, 1, 1, 0]))
        self.assertEqual(3, self.sol.longestSubarray(nums=[0, 0, 1, 1, 1]))
        self.assertEqual(5, self.sol.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
        self.assertEqual(2, self.sol.longestSubarray(nums=[1, 1, 1]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
