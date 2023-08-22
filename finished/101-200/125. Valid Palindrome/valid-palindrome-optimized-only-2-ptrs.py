from unittest import TestCase


def next_an_index(starting_index: int, s: str, step=1):
    end_index = len(s) if step > 0 else 0
    for i in range(starting_index, end_index, step):
        if s[i].isalnum():
            return i
    return len(s) if step > 1 else -1  # 1 step past end of string.


class Solution:
    # noinspection PyMethodMayBeStatic
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = next_an_index(0, s), next_an_index(len(s) - 1, s, step=-1)
        while i < j and i < len(s) and j > -1:
            if s[i] != s[j]:
                return False
            i, j = next_an_index(i + 1, s), next_an_index(j - 1, s, step=-1)
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
        self.assertFalse(self.a.isPalindrome("race a car"))
        self.assertFalse(self.a.isPalindrome("arst"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
