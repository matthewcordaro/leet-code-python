import collections
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def countBits(self, n: int) -> list[int]:
        ans = [0]
        for i in range(1, n+1):
            # multiply num by 2 (even) is adding a zero at the end, so use previous sol
            prev = ans[i >> 1]
            # if it's odd (2n+1), add 1 for the one at the end.
            ans.append(prev + i % 2)
        return ans

class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([0, 1, 1], self.sol.countBits(n=2))
        self.assertEqual([0, 1, 1, 2, 1, 2], self.sol.countBits(n=5))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
