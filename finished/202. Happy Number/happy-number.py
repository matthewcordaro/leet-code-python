import unittest


# O()
class Solution:
  SQUARES = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  def isHappy(self, n: int) -> bool:
    num_seen = {1}
    while n not in num_seen:
      num_seen.add(n)
      n_str = str(n)
      n = 0
      for c in n_str: n += self.SQUARES[int(c)]
    return n == 1


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertTrue(self.sol.isHappy(1))
    self.assertTrue(self.sol.isHappy(19))
    self.assertFalse(self.sol.isHappy(2))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
