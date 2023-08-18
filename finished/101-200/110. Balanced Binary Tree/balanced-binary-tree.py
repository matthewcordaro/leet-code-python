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
    # noinspection PyMethodMayBeStatic
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Compare each side height at each node with dfs
        # -1 means unbalanced
        def dfs(r: Optional[TreeNode]) -> int:
            # None case - balanced
            if r is None:
                return 0

            # Get depth
            ld = dfs(r.left)
            rd = dfs(r.right)

            # check valid depth
            if ld == -1 or rd == -1 or abs(ld - rd) > 1:
                return -1

            # valid, add height
            return 1 + max(ld, rd)

        # any number is balanced here
        return dfs(root) != -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, 1)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
