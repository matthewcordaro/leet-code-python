from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    sol = [1]

    # Calc postfix going left to right
    #  Multiply last item in `sol` to next item in `nums` and append. Skip last num.
    for n in nums[:-1]:
      sol.append(sol[-1] * n)

    # Calc prefix going right to left & combine
    #  Multiply last item in `sol` to next item in `nums` and append. Skip last num.
    cur_mul = 1
    for i, n in reversed(list(enumerate(nums[1:]))):
      cur_mul *= n
      sol[i] *= cur_mul

    return sol


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual([24,12,8,6], self.sol.productExceptSelf([1,2,3,4]))
    self.assertEqual([0,0,9,0,0], self.sol.productExceptSelf([-1,1,0,-3,3]))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
