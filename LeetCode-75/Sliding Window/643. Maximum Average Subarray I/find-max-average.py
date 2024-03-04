from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start, end = 0, k
        current_window_total = sum(nums[:k])
        solution = current_window_total
        while end < len(nums):
            current_window_total = current_window_total - nums[start] + nums[end]
            end += 1
            start += 1
            solution = max(solution, current_window_total)
        return solution/k


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(12.75000, self.sol.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
        self.assertEqual(5.00000, self.sol.findMaxAverage(nums=[5], k=1))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
