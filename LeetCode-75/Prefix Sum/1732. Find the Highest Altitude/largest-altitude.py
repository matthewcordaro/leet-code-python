from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        max_altitude = 0
        for delta in gain:
            altitude += delta
            max_altitude = max(max_altitude, altitude)
        return max_altitude


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, self.sol.largestAltitude(gain=[-5, 1, 5, 0, -7]))
        self.assertEqual(0, self.sol.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
