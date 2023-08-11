from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        median: float = sum(nums1) / 2
        return median


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
