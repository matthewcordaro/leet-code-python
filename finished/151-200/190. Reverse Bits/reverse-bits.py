from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def reverseBits(self, n: int) -> int:
        sol = 0
        for i in range(32):
            sol <<= 1
            sol |= n & 1
            n >>= 1
        return sol


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(964176192, self.sol.reverseBits(0b00000010100101000001111010011100))
        self.assertEqual(3221225471, self.sol.reverseBits(0b11111111111111111111111111111101))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
