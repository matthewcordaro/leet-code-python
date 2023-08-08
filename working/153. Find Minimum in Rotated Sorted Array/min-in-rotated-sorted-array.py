from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findMin(self, nums: list[int]) -> int:
        pass


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, self.sol.findMin([3, 4, 5, 1, 2]))
        self.assertEqual(0, self.sol.findMin([4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(11, self.sol.findMin([11, 13, 15, 17]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
