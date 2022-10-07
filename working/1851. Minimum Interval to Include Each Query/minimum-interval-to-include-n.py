import unittest
from cmath import inf
from typing import List


# O()
class Solution:
  def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    # calc interval size by subtracting: right - left + 1
    size_of_interval = []
    for (left, right) in intervals:
      size_of_interval.append(right - left + 1)

    a_very_large_number = 10 ** 10
    solution = []
    for idq, query in enumerate(queries):
      minimum = a_very_large_number
      for idi, (left, right) in enumerate(intervals):
        # subtract each query from each integer in the interval
        # if 0 between them it's a possible solution
        if left - query <= 0 <= right - query:
          minimum = min(minimum, size_of_interval[idi])
      if minimum is not a_very_large_number:
        solution.append(minimum)
      else:
        solution.append(-1)
    return solution


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual([3, 3, 1, 4], self.sol.minInterval(intervals=[[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5]))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
