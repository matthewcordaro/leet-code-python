from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for op in operations:
            x = x + 1 if op[1] == '+' else x - 1
        return x


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, self.sol.finalValueAfterOperations(["--X", "X++", "X++"]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
