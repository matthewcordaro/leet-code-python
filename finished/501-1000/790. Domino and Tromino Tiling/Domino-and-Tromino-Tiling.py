from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def numTilings(self, num: int) -> int:
        MOD = 1000000007
        tiles = [1, 2, 5]
        for i in range(3, num):
            tiles.append((tiles[i - 3] + tiles[i - 1] * 2) % MOD)
        return tiles[num-1]


# noinspection SpellCheckingInspection
class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_n_1(self):
        self.assertEqual(self.sol.numTilings(1), 1)

    def test_n_2(self):
        self.assertEqual(self.sol.numTilings(2), 2)

    def test_n_3(self):
        self.assertEqual(self.sol.numTilings(3), 5)

    def test_n_4(self):
        self.assertEqual(self.sol.numTilings(4), 11)

    def test_n_5(self):
        self.assertEqual(self.sol.numTilings(5), 24)

    def test_n_20(self):
        self.assertEqual(self.sol.numTilings(20), 3418626)

    def test_n_30(self):
        # The result should be taken modulo 10^9 + 7 as per problem constraints
        self.assertEqual(self.sol.numTilings(30), 312342182)

    def test_edge_case(self):
        self.assertEqual(self.sol.numTilings(1000), 979232805)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
