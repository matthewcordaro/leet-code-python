from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def searchInsert(self, nums: list[int], target: int) -> int:

        def binary_search(low, high):
            if low > high: return low  # Not in list
            mid = high + low // 2
            if target == nums[mid]: return mid
            return binary_search(*(low, mid - 1) if target < nums[mid] else (mid + 1, high))

        return binary_search(0, len(nums)-1)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(2, self.sol.searchInsert(nums = [1,3,5,6], target = 5))
        self.assertEqual(1, self.sol.searchInsert(nums = [1,3,5,6], target = 2))
        self.assertEqual(4, self.sol.searchInsert(nums = [1,3,5,6], target = 7))
        self.assertEqual(0, self.sol.searchInsert(nums = [1,3,5,6], target = 0))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
