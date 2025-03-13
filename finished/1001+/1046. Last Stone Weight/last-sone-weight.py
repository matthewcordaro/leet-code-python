from unittest import TestCase
import heapq


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def lastStoneWeight(self, stones: [int]) -> int:
        stones = [-num for num in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            num = heapq.heappop(stones) - heapq.heappop(stones)
            if num != 0:
                heapq.heappush(stones, num)
        return -stones[0] if stones else 0


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(self.sol.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(self.sol.lastStoneWeight([1]), 1)
        self.assertEqual(self.sol.lastStoneWeight([]), 0)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
