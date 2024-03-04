from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        start, stop = 0, k
        current_total = sum([1 if c in vowels else 0 for c in s[:k]])
        solution = current_total
        while stop < len(s):
            current_total += 1 if s[stop] in vowels else 0
            current_total -= 1 if s[start] in vowels else 0
            solution = max(solution, current_total)
            start += 1
            stop += 1
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.maxVowels(s="abciiidef", k=3))
        self.assertEqual(2, self.sol.maxVowels(s="aeiou", k=2))
        self.assertEqual(2, self.sol.maxVowels(s="leetcode", k=3))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
