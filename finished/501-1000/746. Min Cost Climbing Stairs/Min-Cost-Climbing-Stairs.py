from unittest import TestCase


class Solution:
    # noinspection PyMethodMayBeStatic
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_memoization = [-1 for _ in range(len(cost))]
        def dp_step_calculator (starting_step: int) -> int:
            nonlocal cost, min_memoization
            if starting_step >= len(cost): return 0  # At the top
            if min_memoization[starting_step] == -1:  # undefined, calculate it
                min_memoization[starting_step] = \
                        min(cost[starting_step] + dp_step_calculator(starting_step + 1),
                        cost[starting_step] + dp_step_calculator(starting_step + 2))
            return min_memoization[starting_step]
        return min(dp_step_calculator(0), dp_step_calculator(1))


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        # Example 1 from LeetCode
        cost = [10, 15, 20]
        self.assertEqual(self.sol.minCostClimbingStairs(cost), 15)

    def test_basic_case_2(self):
        # Example 2 from LeetCode
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(self.sol.minCostClimbingStairs(cost), 6)

    def test_minimum_length(self):
        # Test with minimum length array (2 elements)
        cost = [1, 2]
        self.assertEqual(self.sol.minCostClimbingStairs(cost), 1)

    def test_equal_values(self):
        # Test with all equal values
        cost = [5, 5, 5, 5]
        self.assertEqual(self.sol.minCostClimbingStairs(cost), 10)

    def test_alternating_values(self):
        # Test with alternating high-low values
        cost = [20, 1, 20, 1, 20]
        self.assertEqual(self.sol.minCostClimbingStairs(cost), 2)

    def test_decreasing_values(self):
        # Test with decreasing values
        cost = [10, 8, 6, 4, 2]
        self.assertEqual(self.sol.minCostClimbingStairs(cost), 12)

    def test_increasing_values(self):
        # Test with increasing values
        cost = [2, 4, 6, 8, 10]
        self.assertEqual(self.sol.minCostClimbingStairs(cost), 12)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()