from unittest import TestCase


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def twoSum(self, numbers: [int], target: int) -> [int]:
        j = len(numbers) - 1
        for i in range(len(numbers)):
            # if j < i: return []
            while numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_twoSum(self):
        self.assertEqual(self.sol.twoSum([1, 2, 3, 4, 5, 6], 4), [1, 3])


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
