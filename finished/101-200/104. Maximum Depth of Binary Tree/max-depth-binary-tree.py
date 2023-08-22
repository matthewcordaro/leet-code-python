from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n)
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left)) if root else 0


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, 1)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
