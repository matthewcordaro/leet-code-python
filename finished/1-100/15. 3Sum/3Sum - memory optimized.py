import bisect
import unittest
from typing import List


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort. Then working from the outsides in to the (zero most) inflection pt,
        # find solutions: index j, such that i < j < k and num[j] in nums
        nums = sorted(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        inflection_pt = (bisect.bisect_left(nums, 0) + bisect.bisect_right(nums, 0)) // 2
        sol = set()
        for i in range(inflection_pt):
            for k in range(len(nums) - 1, inflection_pt - 1, -1):
                n = -(nums[i] + nums[k])
                j = bisect.bisect_left(nums, n, i + 1, inflection_pt) if n < 0 \
                    else bisect.bisect_left(nums, n, inflection_pt, k - 1)
                if i != j != k and nums[j] == n:
                    sol.add((nums[i], nums[j], nums[k]))
        return sol


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual({(-1, -1, 2), (-1, 0, 1)}, set(self.sol.threeSum([-1, 0, 1, 2, -1, -4])))
        self.assertEqual(set(), set(self.sol.threeSum([0, 1, 1])))
        self.assertEqual({(0, 0, 0)}, set(self.sol.threeSum([0, 0, 0])))
        self.assertEqual({(-1, 0, 1)}, set(self.sol.threeSum([-1, 0, 1, 0])))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
