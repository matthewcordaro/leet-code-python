import unittest


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def jump(self, nums):
    steps = end_current_step = farthest_from_current_step = 0
    for location, jump in enumerate(nums[:-1]):
      farthest_from_current_step = max(farthest_from_current_step, location + jump)
      if location == end_current_step:  # We have reached the end of the current step
        steps += 1
        end_current_step = farthest_from_current_step
    return steps


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
