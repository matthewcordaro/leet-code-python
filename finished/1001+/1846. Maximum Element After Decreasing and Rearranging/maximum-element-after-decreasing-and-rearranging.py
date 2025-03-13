from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(2, self.sol.maximumElementAfterDecrementingAndRearranging(arr=[2, 2, 1, 2, 1]))
        self.assertEqual(3, self.sol.maximumElementAfterDecrementingAndRearranging(arr=[100, 1, 1000]))
        self.assertEqual(5, self.sol.maximumElementAfterDecrementingAndRearranging(arr=[1, 2, 3, 4, 5]))
        self.assertEqual(3, self.sol.maximumElementAfterDecrementingAndRearranging(arr=[73, 98, 9]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
