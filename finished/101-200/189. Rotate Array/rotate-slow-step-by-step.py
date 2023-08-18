import unittest
from typing import List


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def rotate(self, nums: List[int], k: int):
        k %= len(nums)  # avoid extra rotation
        while (k := k - 1) >= 0:
            t = nums[-1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = t
        return nums


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], self.sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
