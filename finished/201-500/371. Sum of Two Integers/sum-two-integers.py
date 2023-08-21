import unittest


# O(b) b = number of bits
class Solution:
    # noinspection PyMethodMayBeStatic
    def getSum(self, a: int, b: int) -> int:
        # Mask to handle maximum carry for negative addition
        # (Negative number addition via positive way)
        while (b & 0xFFFFFFFF) > 0:
            carry = (a & b) << 1
            a = (a ^ b)  # poor man's addition (addition without carry over)
            b = carry
        # handle negative case
        return (a & 0xFFFFFFFF) if b > 0 else a


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_same_sign(self):
        self.assertEqual(self.sol.getSum(1, 2), 3)
        self.assertEqual(self.sol.getSum(-9, -102), -111)

    def test_diff_sign(self):
        self.assertEqual(self.sol.getSum(100, -102), -2)
        self.assertEqual(self.sol.getSum(-100, 555), 455)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
