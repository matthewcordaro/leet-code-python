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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        solution: [int] = []
        self.helper(root, solution, 0)
        return solution

    def helper(self, root: Optional[TreeNode], solution, level: int):
        if root is not None:
            if len(solution) <= level:
                solution.append(root.val)
            self.helper(root.right, solution, level + 1)
            self.helper(root.left, solution, level + 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_solution(self):
    #   self.assertEqual(self.sol.rightSideView([]), 0)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
