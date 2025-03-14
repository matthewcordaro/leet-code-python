from unittest import TestCase


class Solution:
    # noinspection PyMethodMayBeStatic
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) <= 2: return min(cost)
        # Calculate from the top step down
        memo = [-1 for _ in range(len(cost))]
        memo[len(cost) - 1] = cost[len(cost) - 1]  # last step cost
        memo[len(cost) - 2] = cost[len(cost) - 2]  # second to last step cost
        for step_number in reversed(range(0, len(cost)-2)):
            memo[step_number] = cost[step_number] + min(memo[step_number + 1], memo[step_number + 2])
        return min(memo[0], memo[1])


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