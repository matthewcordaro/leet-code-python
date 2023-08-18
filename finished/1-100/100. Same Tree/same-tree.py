import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True  # Both are None
        if not (p and q):
            return False  # One is None
        return p.val == q.val \
            and self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, 1)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
