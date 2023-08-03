from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        delta_days = [0] * len(temperatures)  # all 0s, handles any locally max temps
        search_stack = []  # `(day, temp)`  Note: Decreasing temps.
        for curr_day, curr_temp in enumerate(temperatures):
            # For all previous temps smaller than `curr_temp`, pop the day/temp and calc it's days to larger.
            while search_stack and search_stack[-1][1] < curr_temp:
                prev_day, _ = search_stack.pop()
                delta_days[prev_day] = curr_day - prev_day
            search_stack.append([curr_day, curr_temp])  # Add the current day/temp to stack
        return delta_days


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], self.sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
        self.assertEqual([1, 1, 1, 0], self.sol.dailyTemperatures([30, 40, 50, 60]))
        self.assertEqual([1, 1, 0], self.sol.dailyTemperatures([30, 60, 90]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
