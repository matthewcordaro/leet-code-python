from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def strStr(self, haystack: str, needle: str) -> int:
        return -1 if needle not in haystack else haystack.index(needle)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.strStr(haystack = "sadbutsad", needle = "sad"))
        self.assertEqual(-1, self.sol.strStr(haystack = "leetcode", needle = "leeto"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
