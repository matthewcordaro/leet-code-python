from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O()
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root:
            s_left = s_right = None
            if root.left:
                s_right = self.invertTree(root.left)
            if root.right:
                s_left = self.invertTree(root.right)
            root.left, root.right = s_left, s_right
        return root


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, 1)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
