from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def numDistinct(self, s: str, t: str) -> int:  # t is the string to match
        cache = {}

        def dfs(i: int, j: int) -> int:  # i and j are the respective indices for s & t
            if j == len(t):
                return 1  # matching string is at end; solution found:  +1
            if i == len(s):
                return 0  # no more possibilities to match: +0
            if (i, j) in cache:
                return cache[(i, j)]
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]

        return dfs(0, 0)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.numDistinct(s="rabbbit", t="rabbit"))
        self.assertEqual(5, self.sol.numDistinct(s="babgbag", t="bag"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
