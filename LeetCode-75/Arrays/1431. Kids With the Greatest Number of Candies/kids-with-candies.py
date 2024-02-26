from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
            1 <= candies[i] <= 100
        :type extraCandies: int
            1 <= extraCandies <= 50
        :rtype: List[bool]
        """

        most = max(candies)

        return [c+extraCandies >= most for c in candies]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([True, True, True, False, True],
                         self.sol.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
        self.assertEqual([True, False, False, False, False],
                         self.sol.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
        self.assertEqual([True, False, True],
                         self.sol.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
