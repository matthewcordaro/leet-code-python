from unittest import TestCase


# O()
class Solution:
    def __init__(self):
        self.fib = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                    28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,
                    9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
                    701408733,
                    1134903170, 1836311903)

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
    super(TestSolution)


if __name__ == '__main__':
    main()
