from unittest import TestCase


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def containsDuplicate(self, nums: [int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
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
