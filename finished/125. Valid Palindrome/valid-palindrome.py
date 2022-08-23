import unittest


class Solution:
  def isPalindrome(self, s: str) -> bool:
    # Base cases:
    # check to see if it has any alphanumeric chars
    contains_a_n = False
    for c in s:
      if self.isAlphaNumeric(c):
        contains_a_n = True
        break
    if not contains_a_n:
      return True

    front = 0
    back = -1

    # Compare front to back until pointers pass or match each other.
    # Any non matches, kill.
    while front <= len(s) + back:
      front = self.getNextAlphaLocation(s, front)
      back = self.getNextAlphaLocation(s, back)
      if s[front].lower() != s[back].lower():
        return False
      # next
      front += 1
      back -= 1
    # All match
    return True

  # Returns next valid location
  def getNextAlphaLocation(self, s: str, index: int) -> int:
    # Direction
    step = 1
    if index < 0:
      step = -1
    # Find Next
    while not self.isAlphaNumeric(s[index]):
      index += step
    return index

  @staticmethod
  def isAlphaNumeric(c: chr) -> bool:
    return (
        ord('0') <= ord(c) <= ord('9') or
        ord('a') <= ord(c) <= ord('z') or
        ord('A') <= ord(c) <= ord('Z')
    )


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.a = Solution()

  def test_isPalindrome(self):
    self.assertTrue(self.a.isPalindrome("A man, a plan, a canal: Panama"))
    self.assertTrue(self.a.isPalindrome("arsttsra"))
    self.assertTrue(self.a.isPalindrome("arst. tsra"))
    self.assertTrue(self.a.isPalindrome(""))
    self.assertTrue(self.a.isPalindrome("12345654321"))

    self.assertFalse(self.a.isPalindrome("1234565432345234"))
    self.assertFalse(self.a.isPalindrome("arst"))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
