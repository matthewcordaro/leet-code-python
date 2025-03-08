from enum import nonmember
from unittest import TestCase

# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) float:
        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Get lengths of both arrays
        m, n = len(nums1), len(nums2)
        total_length = m + n  # Total length of combined arrays
        half_length = (total_length + 1) // 2  # Length of the left half we need to find

        # Perform binary search on the smaller array (nums1)
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # Partition index in nums1
            j = half_length - i  # Corresponding partition index in nums2

            # Define boundary values, using infinity for edge cases
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]  # Max value in left part of nums1
            nums1_right_min = float('inf') if i == m else nums1[i]  # Min value in right part of nums1
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]  # Max value in left part of nums2
            nums2_right_min = float('inf') if j == n else nums2[j]  # Min value in right part of nums2

            # Check if this partition is valid
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # If total length is odd, median is the maximum of the left parts
                if total_length % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                # If total length is even, median is average of max of left and min of right
                else:
                    return float((max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2)
            # If partition is invalid, adjust binary search range
            elif nums1_left_max > nums2_right_min:
                right = i - 1  # Too many elements in nums1's left part, search left
            else:
                left = i + 1  # Too few elements in nums1's left part, search right


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(2.0, self.sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
        self.assertEqual(2.5, self.sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
