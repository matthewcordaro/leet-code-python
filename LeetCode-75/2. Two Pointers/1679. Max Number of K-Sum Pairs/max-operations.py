from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                count += 1
                l += 1
                r -= 1
            elif total < k:
                l += 1
            else:
                r -= 1
        return count


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(2, self.sol.maxOperations(nums=[1, 2, 3, 4], k=5))
        self.assertEqual(1, self.sol.maxOperations(nums=[3, 1, 3, 4, 3], k=6))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
