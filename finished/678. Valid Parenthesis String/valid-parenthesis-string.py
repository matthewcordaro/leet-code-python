import unittest


# O(N)
# Min Max Greedy!
class Solution:
  def checkValidString(self, s: str) -> bool:
    # These are for the left parenthesis
    least = most = 0  # These are for tracking left parenthesis
    for c in s:
      if c == '(': least, most = least + 1, most + 1  # Must add LEFT
      elif c == ')': least, most = least - 1, most - 1  # Must remove LEFT
      else: least, most = least - 1, most + 1  # Wildcard can be used both ways
      if most < 0: return False  # More RIGHTS than prior LEFTS + WILDCARDS... kill
      if least < 0: least = 0  # Must use an earlier WILDCARD for a RIGHT or WILDCARD, set to zero
    return least == 0  # Too many LEFTS at finish


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertTrue(self.sol.checkValidString(""))
    self.assertTrue(self.sol.checkValidString("*"))
    self.assertTrue(self.sol.checkValidString("()"))
    self.assertTrue(self.sol.checkValidString("*()"))
    self.assertTrue(self.sol.checkValidString("()*"))
    self.assertTrue(self.sol.checkValidString("(*)"))
    self.assertTrue(self.sol.checkValidString("(())**"))
    self.assertTrue(self.sol.checkValidString("**(())"))
    self.assertTrue(self.sol.checkValidString("()()**"))
    self.assertTrue(self.sol.checkValidString("(((**)"))
    self.assertTrue(self.sol.checkValidString("((()*)"))
    self.assertTrue(self.sol.checkValidString("(((***"))
    self.assertTrue(self.sol.checkValidString("***)))"))
    self.assertTrue(self.sol.checkValidString("(*()))"))
    self.assertTrue(self.sol.checkValidString("(**)))"))
    self.assertFalse(self.sol.checkValidString("("))
    self.assertFalse(self.sol.checkValidString(")"))
    self.assertFalse(self.sol.checkValidString("*("))
    self.assertFalse(self.sol.checkValidString(")*"))
    self.assertFalse(self.sol.checkValidString("***)))("))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
