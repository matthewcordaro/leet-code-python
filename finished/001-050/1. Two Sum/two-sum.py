from unittest import TestCase


# O(n^2)
class Solution:
    # noinspection PyMethodMayBeStatic
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sublist = [target - num for num in nums]
        for i, number in enumerate(nums):
            for j, sub_number in enumerate(sublist[i + 1:]):
                if number == sub_number:
                    return [i, i + j + 1]


# HashMap O(n)
class Solution2:
    # noinspection PyMethodMayBeStatic
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_dictionary = {}
        for i, number in enumerate(nums):
            if number in hash_dictionary.keys():
                return [i, hash_dictionary[number]]
            hash_dictionary[target - number] = i


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()
        self.sol2 = Solution2()

    def test_twoSum(self):
        self.assertEqual(self.sol.twoSum([1, 2, 3, 4, 5, 6], 4), [0, 2])

    def test_twoSum_2(self):
        self.assertEqual(self.sol2.twoSum([1, 2, 3, 4, 5, 6], 4), [2, 0])


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
