import unittest
from typing import List


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def rotate(self, nums: List[int], k: int):
        if (n := len(nums)) <= 1 or (k := k % n) == 0:
            return nums
        # Choose the smallest end of array
        if k < n // 2:
            # Right: go backwards through the first n-k elements, shift them forward k spots
            # put old right, stored, on left
            store = nums[-k:]
            for i in range(n - k - 1, -1, -1):
                nums[i + k] = nums[i]
            nums[:k] = store
        else:
            # Left:  go forwards through the last k elements shift them forwards k spots
            # put old left, stored, on right
            store = nums[:-k]
            for i in range(n - k, n):
                nums[(i + k) % n] = nums[i]
            nums[k:] = store
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
