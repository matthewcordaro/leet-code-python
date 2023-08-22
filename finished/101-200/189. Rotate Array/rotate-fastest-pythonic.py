from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def rotate(self, nums: [int], k: int):
        k %= len(nums)  # avoid extra rotation
        nums[:] = nums[-k:] + nums[:-k]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
