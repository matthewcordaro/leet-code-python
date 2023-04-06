from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def lengthOfLongestSubstring(self, s: str) -> int:
    mx = 0
    cs = set()
    l = r = 0
    while r < len(s):
      if s[r] in cs:
        cs.remove(s[l])
        l +=1
      else:
        cs.add(s[r])
        mx = max(len(cs), mx)
        r += 1
    return mx


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(3, self.sol.lengthOfLongestSubstring("abcabcbb"))
    self.assertEqual(1, self.sol.lengthOfLongestSubstring("bbbbb"))
    self.assertEqual(3, self.sol.lengthOfLongestSubstring("pwwkew"))
    self.assertEqual(2, self.sol.lengthOfLongestSubstring("aab"))
    self.assertEqual(3, self.sol.lengthOfLongestSubstring("dvdf"))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
