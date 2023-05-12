from bisect import insort
from unittest import TestCase


# O()
class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    self.k = k
    self.numbers = sorted(nums)

  def add(self, val: int) -> int:
    insort(self.numbers, val)
    return self.numbers[-self.k]


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(0, self.sol.someFunction(3, [4, 5, 8, 2]))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
