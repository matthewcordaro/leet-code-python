from unittest import TestCase


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def characterReplacement(self, s: str, k: int) -> int:
    mx = kp = 0
    cs = set()
    l = r = m = 0
    while r < len(s):
      if s[r] in cs:
        cs.remove(s[l])
        l += 1
      else:
        cs.add(s[r])
        mx = max(len(cs), mx)
        r += 1
    return mx



class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(4, self.sol.characterReplacement(s = "ABAB", k = 2))
    self.assertEqual(4, self.sol.characterReplacement(s = "AABABBA", k = 1))


def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
