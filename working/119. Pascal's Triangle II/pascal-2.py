import unittest


# O()
class Solution:
  def someFunction(self):
    pass


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(0, self.sol.someFunction())


def main():
    unittest.main()


if __name__ == '__main__':
  main()
