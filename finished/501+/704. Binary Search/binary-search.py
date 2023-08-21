import unittest
from typing import List


# O(log n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def search(self, nums: List[int], target: int) -> int:
        # left and right pointers
        left, right = 0, len(nums) - 1

        while right >= left:
            # i = (left + right) // 2  # overflow issue
            i = left + (right - left) // 2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                right = i - 1
            else:
                left = i + 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4), 4)
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0), 0)
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8], 4), 4)
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8], 0), 0)
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8], 8), 8)
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8], 9), -1)
        self.assertEqual(self.sol.search([0, 1, 2, 3, 4, 5, 6, 7, 8], -1), -1)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
