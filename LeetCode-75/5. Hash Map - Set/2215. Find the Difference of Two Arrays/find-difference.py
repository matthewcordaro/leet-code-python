from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        answer1, answer2 = [], []
        for num in nums1:
            if num not in nums2:
                answer1.append(num)
        for num in nums2:
            if num not in nums1:
                answer2.append(num)
        return [answer1, answer2]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertListEqual([[1, 3], [4, 6]], self.sol.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
        self.assertListEqual([[3], []], self.sol.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
