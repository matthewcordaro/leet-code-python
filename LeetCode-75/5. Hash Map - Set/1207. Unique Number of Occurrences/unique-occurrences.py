from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Counter or default dict better. Using dict to show lower level solution.
        totals = dict()
        for item in arr:
            totals[item] = totals.get(item, 0) + 1
        uc = set(totals.values())  # unique counts
        return len(totals) == len(uc)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertFalse(self.sol.uniqueOccurrences(arr=[1, 2]))

        self.assertTrue(self.sol.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
        self.assertTrue(self.sol.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
