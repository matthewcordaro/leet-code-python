import collections
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def hammingWeight(self, n: int) -> int:
        return collections.Counter(bin(n)[2:]).get("1", 0)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.hammingWeight(n=0b00000000000000000000000000001011))
        self.assertEqual(1, self.sol.hammingWeight(n=0b00000000000000000000000010000000))
        self.assertEqual(31, self.sol.hammingWeight(n=0b11111111111111111111111111111101))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
