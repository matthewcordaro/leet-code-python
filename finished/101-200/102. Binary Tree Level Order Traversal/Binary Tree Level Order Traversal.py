import unittest
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) Speed, O(n) Memory
class Solution:
    def __init__(self):
        self.solution: [[int]] = None

    def traverse(self, node: Optional[TreeNode], level: int):
        if not node:
            return

        if len(self.solution) == level:
            self.solution.append([])  # First time at level

        self.solution[level].append(node.val)
        self.traverse(node.left, level + 1)
        self.traverse(node.right, level + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.solution = []
        self.traverse(root, 0)
        return self.solution


def main():
    unittest.main()


if __name__ == '__main__':
    main()
