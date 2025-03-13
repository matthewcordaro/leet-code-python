from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 0:
            return True

        if sx == fx and sy == fy and t == 1:
            return False

        return max(abs(sx - fx), abs(sy - fy)) <= t


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.isReachableAtTime(sx=2, sy=4, fx=7, fy=7, t=6))
        self.assertFalse(self.sol.isReachableAtTime(sx=3, sy=1, fx=7, fy=3, t=3))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
