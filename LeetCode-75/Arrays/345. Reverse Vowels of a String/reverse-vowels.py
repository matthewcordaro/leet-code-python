from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def reverseVowels(self, s: str) -> str:
        s = [c for c in s]  # convert for mutability
        # Vowels in order of prevalence
        vowels = ('e', 'a', 'i', 'o', 'u', 'E', 'A', 'I', 'O', 'U')
        left, right = 0, len(s) - 1
        while True:
            while (left < len(s)
                   and s[left] not in vowels):  # left search
                left += 1
            while (right >= 0
                   and s[right] not in vowels):  # right search
                right -= 1
            if left >= right:  # break the loop if they pass
                break
            s[left], s[right] = s[right], s[left]  # swap vowels
            left, right = left + 1, right - 1  # move ptrs
        return str().join(s)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("aA", self.sol.reverseVowels(s="Aa"))
        self.assertEqual("holle", self.sol.reverseVowels(s="hello"))
        self.assertEqual("leotcede", self.sol.reverseVowels(s="leetcode"))
        self.assertEqual("bob", self.sol.reverseVowels(s="bob"))
        self.assertEqual("veltago", self.sol.reverseVowels(s="voltage"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
