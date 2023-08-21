import unittest


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def climbStairs(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        val = (golden_ratio ** (n + 1) - (1 - golden_ratio) ** (n + 1)) / 5 ** 0.5
        return int(round(val))


class TestSolution(unittest.TestCase):
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
    unittest.main()


if __name__ == '__main__':
    main()
