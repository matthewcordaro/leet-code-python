from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        return a == a[::-1]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.isPalindrome(212))
        self.assertFalse(self.sol.isPalindrome(-212))
        self.assertFalse(self.sol.isPalindrome(10))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
