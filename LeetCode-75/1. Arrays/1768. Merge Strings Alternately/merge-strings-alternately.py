from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        max_letter = min(len(word1), len(word2))
        for i in range(max_letter):
            merged_word += word1[i] + word2[i]
        if len(word1) > len(word2):
            merged_word += word1[max_letter:]
        elif len(word1) < len(word2):
            merged_word += word2[max_letter:]
        return merged_word


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("apbqcr", self.sol.mergeAlternately(word1="abc", word2="pqr"))
        self.assertEqual("apbqrs", self.sol.mergeAlternately(word1="ab", word2="pqrs"))
        self.assertEqual("apbqcd", self.sol.mergeAlternately(word1="abcd", word2="pq"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
