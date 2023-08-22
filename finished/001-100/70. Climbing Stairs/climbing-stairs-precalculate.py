from unittest import TestCase


# O()
class Solution:
    def __init__(self):
        self.fib = [1, 1, 2, 3, 5, 8]  # quic to define, then calc after
        for n in range(6, 46):
            golden_ratio = (1 + 5 ** 0.5) / 2
            val = (golden_ratio ** (n + 1) - (1 - golden_ratio) ** (n + 1)) / 5 ** 0.5
            self.fib.append(int(round(val)))

    def climbStairs(self, n: int) -> int:
        return self.fib[n]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, self.sol.climbStairs(1))
        self.assertEqual(2, self.sol.climbStairs(2))
        self.assertEqual(3, self.sol.climbStairs(3))
        self.assertEqual(5, self.sol.climbStairs(4))
        self.assertEqual(8, self.sol.climbStairs(5))
        self.assertEqual(1836311903, self.sol.climbStairs(46))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
