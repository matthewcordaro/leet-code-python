import unittest


# O()
class Solution:
  def __init__(self):
    self.fibnocci = [1, 1]

  def climbStairs(self, n: int) -> int:
    if n >= len(self.fibnocci):
      for i in range(len(self.fibnocci), n+1):
        self.fibnocci.append(self.fibnocci[i - 1] + self.fibnocci[i - 2])
    return self.fibnocci[n]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(1, self.sol.climbStairs(1))
    self.assertEqual(2, self.sol.climbStairs(2))
    self.assertEqual(3, self.sol.climbStairs(3))
    self.assertEqual(5, self.sol.climbStairs(4))
    self.assertEqual(8, self.sol.climbStairs(5))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
