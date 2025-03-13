from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        max_width = 10 ** 5  # Constant
        l = r = 0
        total = nums[l]
        width = max_width + 1
        while True:
            current_width = r - l + 1
            if total >= target:
                # Update if needed
                if current_width < width:
                    width = current_width
                # Shrink
                total -= nums[l]
                l += 1
            else:
                # Expand
                r += 1
                if r == len(nums):  # Check for ending condition
                    return 0 if width > max_width else width  # Return if a window was found
                total += nums[r]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.minSubArrayLen(target=7, nums=[5]))
        self.assertEqual(1, self.sol.minSubArrayLen(target=7, nums=[7]))
        self.assertEqual(1, self.sol.minSubArrayLen(target=7, nums=[9]))
        self.assertEqual(2, self.sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
        self.assertEqual(1, self.sol.minSubArrayLen(target=4, nums=[1, 4, 4]))
        self.assertEqual(0, self.sol.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))

def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
