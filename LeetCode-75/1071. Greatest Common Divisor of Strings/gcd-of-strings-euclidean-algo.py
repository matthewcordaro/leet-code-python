from unittest import TestCase


# O()
class Solution(object):
    # noinspection PyMethodMayBeStatic
    def gcdOfStrings(self, str1, str2):
        """
        For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e.,
        t is concatenated with itself one or more times). Given two strings str1 and str2, return the largest string
        x such that x divides both str1 and str2.

        :type str1: str
        :type str2: str
        :rtype: str
        """

        # Fast validity check. (Must match if they repeat.)
        if str1 + str2 != str2 + str1:
            return ""

        # Euclidean algorithm (subtraction version)
        l1, l2 = len(str1), len(str2)
        while l1 != l2:
            if l1 > l2:
                l1 = l1 - l2
            else:
                l2 = l2 - l1

        return str1[:l1]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("ABC", self.sol.gcdOfStrings(str1="ABCABC", str2="ABC"))
        self.assertEqual("AB", self.sol.gcdOfStrings(str1="ABABAB", str2="ABAB"))
        self.assertEqual("", self.sol.gcdOfStrings(str1="LEET", str2="CODE"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
