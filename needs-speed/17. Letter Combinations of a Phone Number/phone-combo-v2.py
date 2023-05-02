from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def letterCombinations(self, digits: str) -> list[str]:
    if len(digits) == 0: return []  # Blank Case

    t9_dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    solution = []

    # IDEA: Storing pairs to not recalculate
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
