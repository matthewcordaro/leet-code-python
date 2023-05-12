import unittest


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def jump(self, nums: list[int]) -> int:
    jump_to = [num + index for index, num in enumerate(nums[:-1])]
    destination = len(nums) - 1
    total_jumps = 0
    # Working backwards from the end, take the earliest possible jump forward, repeat
    while destination > 0:
      for jumped_from, furthest_destination in enumerate(jump_to):
        if furthest_destination >= destination:
          destination = jumped_from
          total_jumps += 1
          break
    return total_jumps


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(2, self.sol.jump([2,3,1,1,4]))
    self.assertEqual(2, self.sol.jump([2,3,0,1,4]))

def main():
    unittest.main()


if __name__ == '__main__':
  main()
