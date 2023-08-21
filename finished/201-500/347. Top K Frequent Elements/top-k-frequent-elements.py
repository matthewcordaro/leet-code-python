import heapq
import unittest
from collections import defaultdict
from typing import List


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)  # start frequency counting from 0
        for num in nums:
            freq[num] -= 1  # go negative for heapq
        heap = []
        for num, quantity in freq.items():
            heapq.heappush(heap, (quantity, num))
        nums = []  # repurpose nums for the solution
        while (k := k - 1) >= 0:
            nums.append(heapq.heappop(heap)[1])
        return nums


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
