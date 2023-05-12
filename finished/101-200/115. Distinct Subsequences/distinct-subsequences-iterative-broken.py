
from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def numDistinct(self, s:str, t:str) -> int:  # t is the string to match
    ls, lt = len(s), len(t)
    cache = [[0 for _ in range(ls+1)] for _ in range(lt+1)]
    for i in range(ls+1): cache[i][0] = 1  # initialize for
    for i in range(1, ls+1):
        for j in range(1, lt+1):
            cache[i][j] = cache[i-1][j]
            if s[i-1] == t[j-1]:
                cache[i][j] += cache[i-1][j-1]
    return cache[s][t]


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(3, self.sol.numDistinct(s = "rabbbit", t = "rabbit"))
    self.assertEqual(5, self.sol.numDistinct(s = "babgbag", t = "bag"))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
