from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        This is a "good enough" solution. There's definitely a quicker way by moving all the items to the end of the
        list only when needed, but it won't save more than `n` operations.  This is more debuggable.
        """

        # Move all the items to the end of the list, right to left, so we don't collide.
        i = m
        while i > 0:
            i -= 1
            nums1[i + n] = nums1[i]

        # Clear moved items for debugging sanity.  Can be removed after solving.
        # for j in range(0, n):
        #     nums1[j] = 0

        # Merge over until one list left
        i, i1, i2 = 0, n, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                nums1[i] = nums1[i1]
                i1 += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
            i += 1

        # Copy Left
        while i1 < len(nums1):
            nums1[i] = nums1[i1]
            i1 += 1
            i += 1

        # Copy Right
        while i2 < len(nums2):
            nums1[i] = nums2[i2]
            i2 += 1
            i += 1


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        self.sol.merge(nums1, m=3, nums2=[2, 5, 6], n=3)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)

        nums1 = [1]
        self.sol.merge(nums1, m=1, nums2=[], n=0)
        self.assertEqual([1], nums1)

        nums1 = [0]
        self.sol.merge(nums1, m=0, nums2=[1], n=1)
        self.assertEqual([1], nums1)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
