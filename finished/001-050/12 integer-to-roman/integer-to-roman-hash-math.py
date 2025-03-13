from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def intToRoman(self, num: int) -> str:
        digit_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X",
                            9: "IX", 5: "V", 4: "IV", 1: "I"}
        solution = ""
        for digit in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while num >= digit:
                solution += digit_dict[digit]
                num -= digit
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
