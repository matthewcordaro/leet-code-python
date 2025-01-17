from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = int(str(abs(x))[::-1])
        x = -1 * x if negative else x
        return x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(321, self.sol.reverse(123))
        self.assertEqual(-321, self.sol.reverse(-123))
        self.assertEqual(0, self.sol.reverse(0))
        self.assertEqual(0, self.sol.reverse(2 ** 31 - 1))
        self.assertEqual(0, self.sol.reverse(1534236469))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
