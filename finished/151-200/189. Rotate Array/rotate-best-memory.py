from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def rotate(self, nums: [int], k: int):
        if (n := len(nums)) <= 1 or (k := k % n) == 0:
            return nums

        def rev(left=0, right=(n - 1)):  # reverse nums between left to right, inclusive
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]  # swap
                left, right = left + 1, right - 1  # move inward

        rev()  # whole list
        rev(right=k - 1)  # then the first k elements
        rev(left=k)  # then the rest
        return nums


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], self.sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
