from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def removeDuplicates(self, nums: list[int]) -> int:
        base_pointer = 0
        seeking_pointer = 1
        length = len(nums)
        while seeking_pointer < length:
            if base_pointer == seeking_pointer or \
                    nums[base_pointer] == nums[seeking_pointer]:
                seeking_pointer += 1
                continue
            diff = seeking_pointer - base_pointer
            if diff <= 2:
                base_pointer = seeking_pointer
                continue
            base_pointer += 2
            while seeking_pointer < length:
                nums[seeking_pointer - diff + 2] = nums[seeking_pointer]
                seeking_pointer += 1
            seeking_pointer = base_pointer + 1
            length -= diff - 2
        if seeking_pointer - base_pointer >= 2:
            length = base_pointer + 2
        return length


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        nums = [1, 1, 1]
        r_nums = nums.copy()
        ret = self.sol.removeDuplicates(r_nums)
        self.assertEqual(2, ret)
        self.assertListEqual([1, 1], r_nums[:2])

        nums = [1, 1, 1, 2, 2, 3]
        r_nums = nums.copy()
        ret = self.sol.removeDuplicates(r_nums)
        self.assertEqual(5, ret)
        self.assertListEqual([1, 1, 2, 2, 3], r_nums[:5])

        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        r_nums = nums.copy()
        ret = self.sol.removeDuplicates(r_nums)
        self.assertEqual(7, ret)
        self.assertListEqual([0, 0, 1, 1, 2, 3, 3], r_nums[:7])


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
