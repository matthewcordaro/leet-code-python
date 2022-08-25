import unittest


# O()
class Solution:
  # FUNCTION HERE
  pass


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(1, 1)


def main():
    unittest.main()


if __name__ == '__main__':
  main()
