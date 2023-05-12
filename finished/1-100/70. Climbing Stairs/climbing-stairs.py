import unittest


# O()
class Solution:
  def climbStairs(self, n: int) -> int:
    golden_ratio = (1 + 5 ** 0.5) / 2
    val = (golden_ratio ** (n+1) - (1 - golden_ratio) ** (n+1)) / 5 ** 0.5
    return int(round(val))


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(self.sol.someFunction([]), 0)


def main():
  unittest.main()


if __name__ == '__main__':
  main()
