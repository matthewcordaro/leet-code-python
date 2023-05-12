from __future__ import annotations

import unittest
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left: TreeNode = None, right: TreeNode = None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def __init__(self):
    self.solution: List[int] = []

  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root is None: return []
    self.solution = [root.val]
    self.helper(root, 0)
    return self.solution

  def helper(self, root: Optional[TreeNode], level: int):
    if root is None: return
    next_level = level + 1

    if len(self.solution) <= next_level:
      if root.right: self.solution.append(root.right.val)
      elif root.left: self.solution.append(root.left.val)

    self.helper(root.right, next_level)
    self.helper(root.left, next_level)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  # def test_solution(self):
  #   self.assertEqual(self.sol.rightSideView([]), 0)


def main():
  unittest.main()


if __name__ == '__main__':
  main()
