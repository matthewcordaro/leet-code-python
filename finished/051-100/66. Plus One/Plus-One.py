from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def plusOne(self, digits: list[int]) -> list[int]:
        digits.reverse()
        overflow = True  # this will add one to the first digit
        for i in range(len(digits)):
            if overflow:  # check for previous overflow
                digits[i] += 1
                overflow = digits[i] >= 10  # if new overflow set 0
                if overflow: digits[i] = 0
        if overflow: digits.append(1)
        digits.reverse()
        return digits


# noinspection SpellCheckingInspection
class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        # Basic cases
        self.assertListEqual([1, 2, 4], self.sol.plusOne([1, 2, 3]))
        self.assertListEqual([4, 0], self.sol.plusOne([3, 9]))

        # Case with all 9's
        self.assertListEqual([1, 0, 0, 0], self.sol.plusOne([9, 9, 9]))

        # Single digit cases
        self.assertListEqual([2], self.sol.plusOne([1]))
        self.assertListEqual([1, 0], self.sol.plusOne([9]))

        # Larger numbers
        self.assertListEqual([1, 0, 0, 0, 0], self.sol.plusOne([9, 9, 9, 9]))
        self.assertListEqual([2, 3, 4, 5, 0], self.sol.plusOne([2, 3, 4, 4, 9]))

        # Zero case
        self.assertListEqual([1], self.sol.plusOne([0]))

def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
