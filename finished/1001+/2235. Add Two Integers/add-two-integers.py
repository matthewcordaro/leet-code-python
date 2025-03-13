from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def sum(self, num1: int, num2: int) -> int: return num1 + num2


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(17, self.sol.sum(num1=12, num2=5))
        self.assertEqual(-6, self.sol.sum(num1=-10, num2=4))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
