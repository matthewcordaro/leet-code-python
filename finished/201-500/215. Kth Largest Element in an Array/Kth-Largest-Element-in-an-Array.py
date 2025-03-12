import heapq
from unittest import TestCase


# O(n log n) - with sorting approach
# O(n) average case - with quickselect approach
class Solution:
    # noinspection PyMethodMayBeStatic
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        # Basic case from LeetCode example
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(self.sol.findKthLargest(nums, k), 5)

    def test_second_example(self):
        # Second example from LeetCode
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(self.sol.findKthLargest(nums, k), 4)

    def test_single_element(self):
        # Edge case with single element
        nums = [1]
        k = 1
        self.assertEqual(self.sol.findKthLargest(nums, k), 1)

    def test_duplicate_elements(self):
        # Array with duplicate elements
        nums = [3, 3, 3, 3, 3, 3]
        k = 2
        self.assertEqual(self.sol.findKthLargest(nums, k), 3)

    def test_negative_numbers(self):
        # Array with negative numbers
        nums = [-1, -2, -3, -4, 0]
        k = 2
        self.assertEqual(self.sol.findKthLargest(nums, k), -1)

    def test_large_k(self):
        # Testing with k equal to array length (smallest element)
        nums = [1, 2, 3, 4, 5]
        k = 5
        self.assertEqual(self.sol.findKthLargest(nums, k), 1)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
