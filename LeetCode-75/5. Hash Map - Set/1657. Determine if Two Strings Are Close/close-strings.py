from collections import Counter
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):  # Quick check
            return False
        counter1, counter2 = Counter(word1), Counter(word2)
        letter_differences = counter1.keys() - counter2.keys()  # Operation 1
        count_differences = Counter(counter1.values()) - Counter(counter2.values())  # Operation 2
        return len(letter_differences) == len(count_differences) == 0


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.closeStrings(word1="abc", word2="bca"))
        self.assertTrue(self.sol.closeStrings(word1="cabbba", word2="abbccc"))
        self.assertTrue(self.sol.closeStrings(word1="cbbbaa", word2="abbccc"))

        self.assertFalse(self.sol.closeStrings(word1="a", word2="aa"))
        self.assertFalse(self.sol.closeStrings(word1="ab", word2="aa"))
        self.assertFalse(self.sol.closeStrings(word1="uau", word2="ssx"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
