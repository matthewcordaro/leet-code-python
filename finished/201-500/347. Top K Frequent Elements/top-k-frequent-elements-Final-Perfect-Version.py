import unittest
from collections import Counter
from typing import List


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        # Documentation on Python site wrong.
        # Expected: 1st argument
        # Actual:   2nd argument (items to test)
        self.assertEqual([1, 2], self.sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
        self.assertEqual([1], self.sol.topKFrequent(nums=[1], k=1))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
