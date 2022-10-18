import unittest


# O()
class Solution:
  SQUARE_NUMBERS = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

  def isHappy(self, n: int) -> bool:
    numbers_hit = set()
    sum_square = n
    while True:
      sum_square = self.sum_square_of_digits(sum_square)
      if sum_square == 1: return True
      if sum_square in numbers_hit: return False
      numbers_hit.add(sum_square)

  def sum_square_of_digits(self, n: int) -> int:
    s = str(n)
    sum_square = 0
    for c in s:
      sum_square += self.SQUARE_NUMBERS[int(c)]
    return sum_square


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
