import heapq
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        distances = []
        for point in points:
            x, y = point
            distance = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(distances, (distance, point))
        closest_heap_points = heapq.nsmallest(k, distances)
        points = [point for _, point in closest_heap_points]
        return points


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([[3, 3], [-2, 4]], self.sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
