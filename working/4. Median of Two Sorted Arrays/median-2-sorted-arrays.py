from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)
        even = total % 2 is 0
        mid = (len(nums1) + len(nums2)) // 2
        i1, i2 = len(nums1) // 2, len(nums2) // 2  # Starting positions for search
        found = False
        while not found:
            if nums1[i1] > nums2[i2]:
                # i2 increase and i1 decrease
                pass
        return mid


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
