from unittest import TestCase


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def containsDuplicate(self, nums: [int]) -> bool:
        hash_dictionary = {}
        for i, number in enumerate(nums):
            if number in hash_dictionary.keys():
                return True
            hash_dictionary[number] = i
        return False


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_containsDuplicate(self):
        self.assertFalse(self.sol.containsDuplicate([1, 2, 3, 4, 5, 6]))

        self.assertTrue(self.sol.containsDuplicate([1, 2, 3, 4, 5, 6, 6]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
