from unittest import TestCase
from collections import Counter


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        return [num for num, _ in Counter(nums).most_common(k)]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        # Documentation on Python site wrong.
        # Expected: 1st argument
        # Actual:   2nd argument (items to test)
        self.assertEqual([1, 2], self.sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
        self.assertEqual([1], self.sol.topKFrequent(nums=[1], k=1))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
