from unittest import TestCase


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    # noinspection PyMethodMayBeStatic
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while True:
            g = (low + high) >> 1
            ans = guess(g)
            if ans == 0:
                return g
            elif ans == 1:
                low = g + 1
            else:
                high = g - 1


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
