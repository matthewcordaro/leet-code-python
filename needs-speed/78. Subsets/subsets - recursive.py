from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def subsets(self, nums: list[int]) -> list[list[int]]:
    if len(nums) == 0: return [[]]
    solution = []
    for i, n in enumerate(nums):
      # calculate all solutions further down the tree
      further_solutions = self.subsets(nums[i+1:])
      # Now extend back with the including and excluding n:
      solution.extend(further_solutions)
      for fs in further_solutions:
        solution.append(fs.append(n))
    return solution

class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    ans = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    self.assertEqual(ans, self.sol.subsets(nums = [1,2,3]))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
