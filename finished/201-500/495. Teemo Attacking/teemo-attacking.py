from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        poisoned = 0
        i = 0
        while i <= len(timeSeries) - 2:
            if timeSeries[i] + duration - 1 >= timeSeries[i + 1]:
                poisoned += timeSeries[i + 1] - timeSeries[i]
            else:
                poisoned += duration
            i += 1
        poisoned += duration
        return poisoned


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(4, self.sol.findPoisonedDuration(timeSeries=[1, 4], duration=2))
        self.assertEqual(3, self.sol.findPoisonedDuration(timeSeries=[1, 2], duration=2))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
