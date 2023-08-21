from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def maxArea(self, height: list[int]) -> int:
        max_area = 0  # Solution
        left, right = 0, len(height) - 1
        # Two Pointers: Test until converged.
        while left < right:
            test_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, test_area)
            # Greedy: always update the limiting height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(49, self.sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(1, self.sol.maxArea([1, 1]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
