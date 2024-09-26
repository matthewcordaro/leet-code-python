from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev_numeral = s[0]
        ans = roman_numerals[prev_numeral]
        for numeral in s[1:]:
            ans += roman_numerals[numeral]
            if roman_numerals[prev_numeral] < roman_numerals[numeral]:
                ans -= roman_numerals[prev_numeral] * 2
            prev_numeral = numeral
        return ans


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.romanToInt(s="III"))
        self.assertEqual(58, self.sol.romanToInt(s="LVIII"))
        self.assertEqual(1994, self.sol.romanToInt(s="MCMXCIV"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
