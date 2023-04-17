from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def uniquePaths(self, m: int, n: int) -> int:
    # col, then row ... [[_ for n of col] for r of row]
    path = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # Swap start and finish. But start at 1,1; 0th row & 0th col become 0 val helpers
    path[0][1] = 1  # Hack an initialization
    for mi in range(m):
      for ni in range(n):
        path[mi+1][ni+1] = path[mi+1][ni] + path[mi][ni+1]
    return path[m][n]




class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(28, self.sol.uniquePaths(m = 3, n = 7))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
