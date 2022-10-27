import unittest
from typing import List


# O()
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    solution = {}
    for string in strs:
      sid = tuple(sorted(string))
      if sid in solution.keys():
        solution[sid].append(string)
      else:
        solution[sid] = [string]
    return list(solution.values())


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual([''], self.sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def main():
  unittest.main()


if __name__ == '__main__':
  main()
