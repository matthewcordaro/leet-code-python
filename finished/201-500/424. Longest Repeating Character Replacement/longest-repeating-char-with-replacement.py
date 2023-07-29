from collections import defaultdict
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def characterReplacement(self, s: str, k: int) -> int:
        solution = 0
        left = 0
        char_freq = defaultdict(lambda: 0)  # frequency of letters in the window
        for right in range(len(s)):
            char_freq[s[right]] += 1  # add new letter when expanding window
            # Greedy: We only care about the most frequent char in the window.
            window_size = right - left + 1
            # If the most frequent char in the window plus the allowed k changes
            # is >= the window size; a valid window -> update the max
            if k + max(char_freq.values()) >= window_size:
                solution = max(solution, window_size)
            else:  # invalid window -> slide the window
                char_freq[s[left]] -= 1
                left += 1
                if char_freq[s[left]] == 0:  # keep memory in check but may thrash
                    char_freq.pop(s[left])
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(4, self.sol.characterReplacement(s="ABAB", k=2))
        self.assertEqual(1, self.sol.characterReplacement(s="AABABBA", k=1))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
