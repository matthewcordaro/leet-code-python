import unittest


# O()
class Solution:
  def __init__(self):
    self.fib = [1, 1, 2, 3, 5, 8]  # quic to define, then calc after
    for n in range(6, 46):
      golden_ratio = (1 + 5 ** 0.5) / 2
      val = (golden_ratio ** (n + 1) - (1 - golden_ratio) ** (n + 1)) / 5 ** 0.5
      self.fib.append(int(round(val)))

  def climbStairs(self, n: int) -> int:
    return self.fib[n]


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(self.sol.someFunction([]), 0)


def main():
  unittest.main()


if __name__ == '__main__':
  main()
