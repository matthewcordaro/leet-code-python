from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def reverseString(self, s: list[str]) -> None:
        for i in range(int(len(s) / 2)):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        hello = ["h", "e", "l", "l", "o"]
        self.sol.reverseString(hello)
        self.assertEqual(["o", "l", "l", "e", "h"], hello)

        hannah = ["H", "a", "n", "n", "a", "h"]
        self.sol.reverseString(hannah)
        self.assertEqual(["h", "a", "n", "n", "a", "H"], hannah)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
