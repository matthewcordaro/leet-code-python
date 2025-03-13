from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findMin(self, nums: list[int]) -> int:
        def rev_bin(low=0, high=len(nums) - 1) -> int:
            # Pick the smallest when we have two remaining
            if low + 1 == high:
                return min(nums[high], nums[low])
            mid = (high + low) // 2  # not integer safe
            # Which half do we continue the search in?
            return rev_bin(low, mid) if nums[low] > nums[mid] else rev_bin(mid, high)

        # Check if only one number OR in order already
        return nums[0] if len(nums) == 1 or nums[0] < nums[-1] else rev_bin()


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
