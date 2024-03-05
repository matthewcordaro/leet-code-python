from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("blue is sky the", self.sol.reverseWords(s="the sky is blue"))
        self.assertEqual("world hello", self.sol.reverseWords(s="  hello world  "))
        self.assertEqual("example good a", self.sol.reverseWords(s="a good   example"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
