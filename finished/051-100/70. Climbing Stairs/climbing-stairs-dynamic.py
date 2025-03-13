from unittest import TestCase


# O()
class Solution:
    def __init__(self):
        self.fibonacci = [1, 1]

    def climbStairs(self, n: int) -> int:
        if n >= len(self.fibonacci):
            for i in range(len(self.fibonacci), n + 1):
                self.fibonacci.append(self.fibonacci[i - 1] + self.fibonacci[i - 2])
        return self.fibonacci[n]


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
