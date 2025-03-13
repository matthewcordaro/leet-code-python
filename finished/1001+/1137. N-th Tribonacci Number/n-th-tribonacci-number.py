from unittest import TestCase


# O()
class Solution:
    tri = [0, 1, 1]

    # noinspection PyMethodMayBeStatic
    def tribonacci(self, n: int) -> int:
        while len(self.tri) <= n:
            self.tri.append(self.tri[-1] + self.tri[-2] + self.tri[-3])
        return self.tri[n]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution_A(self):
        self.assertEqual(0, self.sol.tribonacci(n=0))
        self.assertEqual(1, self.sol.tribonacci(n=1))
        self.assertEqual(1, self.sol.tribonacci(n=2))
        self.assertEqual(2, self.sol.tribonacci(n=3))
        self.assertEqual(4, self.sol.tribonacci(n=4))

    def test_solution_B(self):
        self.assertEqual(1389537, self.sol.tribonacci(n=25))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
