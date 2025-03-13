from __future__ import annotations
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> [int]:
        solution: [int] = []
        self.helper(root, solution, 0)
        return solution

    def helper(self, root: TreeNode | None, solution, level: int):
        if root is not None:
            if len(solution) <= level:
                solution.append(root.val)
            self.helper(root.right, solution, level + 1)
            self.helper(root.left, solution, level + 1)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_solution(self):
    #   self.assertEqual(self.sol.rightSideView([]), 0)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
