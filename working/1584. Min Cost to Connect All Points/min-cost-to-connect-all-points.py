from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        @summary: https://leetcode.com/problems/min-cost-to-connect-all-points/
        @param points: The points on the 2D-plane, where points[i] = [xi, yi]
        @return: The minimum manhattan distance cost to make all points connected.
        (All points are connected if there is exactly one simple path between any two points.)
        """
        
        def manhattan_distance(p1, p2): 
            """
            @summary: Calculate the manhattan distance between two points
            @param p1: The first point
            @param p2: The second point
            @return: The manhattan distance between the two points
            """
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        pass


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(20, self.sol.minCostConnectPoints(
            points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
