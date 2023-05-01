from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def letterCombinations(self, digits: str) -> list[str]:
    if len(digits) == 0: return []  # Blank Case

    t9_dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    solution = []

    def depth_first_search(working_solution: str, position: int):
      # Base Case:  End of solution tree
      if position == len(digits):
        solution.append(working_solution)
        return  # Backtrack

      # Explore:  Try adding each letter to the working solution
      digit = digits[position]
      for c in t9_dict[digit]:
        depth_first_search(working_solution + c, position + 1)
        # Backtrack:  No need to undo variables, not modified

    depth_first_search("", 0)
    return solution


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    ans = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    test = self.sol.letterCombinations("23")
    self.assertListEqual(sorted(ans), sorted(test))
    self.assertEqual([], sorted(self.sol.letterCombinations("")))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
