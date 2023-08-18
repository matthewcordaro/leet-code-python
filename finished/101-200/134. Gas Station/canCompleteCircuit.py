from unittest import TestCase


# O()
# Math Property...
# First, make sure enough total gas for full loop. (Then at least 1 solution must exist.)
# Solution = First index (i) where the tank will never drop below 0 before end.
# (Because to get to that index from index 0, gas had to come from end of list)
class Solution:
    # noinspection PyMethodMayBeStatic
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        tank = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < 0:  # Tank went negative, reset.
                tank, start = 0, i + 1
        return start


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
