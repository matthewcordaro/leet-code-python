from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        only lowercase letters
        0 <= s.length <= 100
        0 <= t.length <= 104
        """
        i = 0
        for cs in s:
            i = t.find(cs, i) + 1
            if i == 0:
                return False
        return True


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertFalse(self.sol.isSubsequence(s="aaaaaa", t="bbaaaa"))
        self.assertFalse(self.sol.isSubsequence(s="axc", t="ahbgdc"))
        self.assertFalse(self.sol.isSubsequence(s="axc", t=""))
        self.assertTrue(self.sol.isSubsequence(s="abc", t="ahbgdc"))
        self.assertTrue(self.sol.isSubsequence(s="", t="ahbgdc"))
        self.assertTrue(self.sol.isSubsequence(s="", t=""))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
