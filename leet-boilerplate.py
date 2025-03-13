from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def someFunction(self):
        pass


# noinspection SpellCheckingInspection
class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.someFunction())


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
