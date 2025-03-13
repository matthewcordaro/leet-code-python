from typing import Optional
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs_tree(root: Optional[TreeNode]) -> list[int]:
            l: list[int] = []
            if not root.left and not root.right:
                l.append(root.val)  # A leaf
            else:
                if root.left:
                    l.extend(dfs_tree(root.left))  # traverse left
                if root.right:
                    l.extend(dfs_tree(root.right))  # traverse right
            return l
        # Compare lists for equality
        return dfs_tree(root1) == dfs_tree(root2)




class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
