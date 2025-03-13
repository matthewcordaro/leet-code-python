from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass

class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    # noinspection SpellCheckingInspection
    def test_solution(self):
        # Existing test cases
        self.assertEqual(3, self.sol.longestCommonSubsequence("abcde", "ace"))
        self.assertEqual(3, self.sol.longestCommonSubsequence(text1="abc", text2="abc"))
        self.assertEqual(0, self.sol.longestCommonSubsequence(text1="abc", text2="def"))

        # Empty strings
        self.assertEqual(0, self.sol.longestCommonSubsequence("", ""))
        self.assertEqual(0, self.sol.longestCommonSubsequence("abc", ""))
        self.assertEqual(0, self.sol.longestCommonSubsequence("", "xyz"))

        # Single character strings
        self.assertEqual(1, self.sol.longestCommonSubsequence("a", "a"))
        self.assertEqual(0, self.sol.longestCommonSubsequence("a", "b"))

        # Longer sequences
        self.assertEqual(4, self.sol.longestCommonSubsequence("AGGTAB", "GXTXAYB"))
        self.assertEqual(5, self.sol.longestCommonSubsequence("ABCDEFG", "ABCDEFG"))

        # Repeated characters
        self.assertEqual(4, self.sol.longestCommonSubsequence("AAAA", "AAAA"))
        self.assertEqual(2, self.sol.longestCommonSubsequence("AAAACC", "CCAAAA"))

        # Non-contiguous subsequences
        self.assertEqual(4, self.sol.longestCommonSubsequence("ABCDGH", "AEDFHR"))

        # Case sensitivity test
        self.assertEqual(0, self.sol.longestCommonSubsequence("ABC", "abc"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
