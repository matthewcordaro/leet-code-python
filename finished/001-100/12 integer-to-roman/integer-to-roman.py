from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def intToRoman(self, num: int) -> str:
        roman_digits = (("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
                        ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
                        ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"), ("", "M", "MM", "MMM"))
        solution = ""
        digits = [int(x) for x in reversed(str(num))]
        for digit, i in enumerate(digits):
            solution = roman_digits[digit][i] + solution
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("MMMDCCXLIX", self.sol.intToRoman(3749))
        self.assertEqual("LVIII", self.sol.intToRoman(58))
        self.assertEqual("MCMXCIV", self.sol.intToRoman(1994))
        self.assertEqual("XIII", self.sol.intToRoman(13))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
