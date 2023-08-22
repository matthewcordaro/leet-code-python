from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]  # +1 for the helping zeros
        for i1 in range(len1 - 1, -1, -1):
            for i2 in range(len2 - 1, -1, -1):
                dp[i1][i2] = dp[i1 + 1][i2 + 1] + 1 if text1[i1] == text2[i2] \
                    else max(dp[i1][i2 + 1], dp[i1 + 1][i2])
        return dp[0][0]  # Solution is now in the root


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.longestCommonSubsequence("abcde", "ace"))
        self.assertEqual(3, self.sol.longestCommonSubsequence(text1="abc", text2="abc"))
        self.assertEqual(0, self.sol.longestCommonSubsequence(text1="abc", text2="def"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
