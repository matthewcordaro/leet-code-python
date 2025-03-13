from unittest import TestCase


class Solution:
    # noinspection PyMethodMayBeStatic
    def isPalindrome(self, s: str) -> bool:
        ans = list()  # Alpha-Numeric-String
        for c in s:
            if c.isalnum():
                ans.append(c.lower())
        for i in range(int(len(ans) / 2)):  # Check from both ends
            if ans[i] != ans[-i - 1]:
                return False
        return True


class TestSolution(TestCase):
    def setUp(self):
        self.a = Solution()

    def test_isPalindrome(self):
        self.assertTrue(self.a.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.a.isPalindrome("arsttsra"))
        self.assertTrue(self.a.isPalindrome("arst. tsra"))
        self.assertTrue(self.a.isPalindrome(""))
        self.assertTrue(self.a.isPalindrome("a"))
        self.assertTrue(self.a.isPalindrome("aa"))
        self.assertTrue(self.a.isPalindrome("aaa"))
        self.assertTrue(self.a.isPalindrome("aaaa"))
        self.assertTrue(self.a.isPalindrome("12345654321"))

        self.assertFalse(self.a.isPalindrome("1234565432345234"))
        self.assertFalse(self.a.isPalindrome("arst"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
