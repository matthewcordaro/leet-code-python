from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[-1]  # initial case
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                candidate = nums[i] + nums[left] + nums[right]
                if abs(candidate - target) < abs(closest_sum - target):
                    closest_sum = candidate  # normalization closer to zero, update
                if candidate == target:  # we found the solution, end early
                    return candidate
                elif candidate > target:  # move appropriate pointer, skip duplicates
                    right -= 1
                    while left < right - 1 and nums[right] == nums[right-1]: right -= 1
                else:
                    left += 1
                    while left + 1 < right and nums[left] == nums[left+1]: left += 1
        return closest_sum


# noinspection SpellCheckingInspection
class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_failed_example_case_1(self):
        nums = [1, 1, 1, 0]
        target = 100
        expected = 3
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))

    def test_failed_example_case_2(self):
        nums = [4,0,5,-5,3,3,0,-4,-5]
        target = -2
        expected = -2  # [-5, 0, 3] = -2
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))


    def test_example_case(self):
        nums = [-1, 2, 1, -4]
        target = 1
        expected = 2  # (-1 + 2 + 1 = 2)
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))


    def test_exact_match(self):
        nums = [0, 0, 0]
        target = 0
        expected = 0
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))


    def test_all_positive(self):
        nums = [1, 2, 3, 4, 5]
        target = 13
        expected = 12
        self.assertEqual(self.sol.threeSumClosest(nums, target), expected)


    def test_all_negative(self):
        nums = [-5, -4, -3, -2, -1]
        target = -8
        expected = -8  # (-3 + -2 + -3 = -8)
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))


    def test_mixed_numbers(self):
        nums = [-5, 2, 3, -2, 4, -1]
        target = 0
        expected = 0  # (-2 + 3 + -1 = 0)
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))


    def test_larger_numbers(self):
        nums = [-1000, 1000, 1000, -1000, 1000, -1000]
        target = 100
        expected = 1000  # (1000 + 0 + 0 = 1000)
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))


    def test_minimal_length(self):
        nums = [1, 1, 1]
        target = 100
        expected = 3  # (1 + 1 + 1 = 3)
        self.assertEqual(expected, self.sol.threeSumClosest(nums, target))

def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
