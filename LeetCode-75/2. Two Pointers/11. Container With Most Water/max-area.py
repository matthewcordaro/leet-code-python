from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def maxArea(self, height: list[int]) -> int:
        current_max = 0
        i, j = 0, len(height) - 1
        while i < j:
            current_length = (j - i)
            if height[i] < height[j]:
                current_max = max(current_max, current_length * height[i])
                i += 1
            else:
                current_max = max(current_max, current_length * height[j])
                j -= 1
        return current_max


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(49, self.sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(1, self.sol.maxArea(height=[1, 1]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
