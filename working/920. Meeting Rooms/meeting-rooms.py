from unittest import TestCase

# O()
class Solution:
    # noinspection PyMethodMayBeStatic

    def can_attend_meetings(self, intervals):
        """
        @param intervals: an array of meeting time intervals
        @return: if a person could attend all meetings
        """
        intervals.sort(key=lambda interval: interval[0])
        for i in range(1, len(intervals)):
            prev_interval, interval = intervals[i - 1], interval[i]
            if interval[0] < prev_interval[1]:
                return False
        return True


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.someFunction())


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
