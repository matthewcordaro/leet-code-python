from typing import Optional
from unittest import TestCase
from tree_node_helpers import create_tree, TreeNode


class Solution:
    # noinspection PyMethodMayBeStatic
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If we hit the end (None), or the solution (val = root.val) return the root.
        if root is None or root.val == val: return root
        # If val is less than root's val, go left, otherwise go right
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_node_exists(self):
        root = create_tree([4, 2, 7, 1, 3])
        result = self.sol.searchBST(root, 2)
        self.assertEqual(result.val, 2)

    def test_node_does_not_exist(self):
        root = create_tree([4, 2, 7, 1, 3])
        result = self.sol.searchBST(root, 5)
        self.assertIsNone(result)

    def test_single_node_exists(self):
        root = create_tree([1])
        result = self.sol.searchBST(root, 1)
        self.assertEqual(result.val, 1)

    def test_single_node_does_not_exist(self):
        root = create_tree([1])
        result = self.sol.searchBST(root, 2)
        self.assertIsNone(result)

    def test_empty_tree(self):
        root = create_tree([])
        result = self.sol.searchBST(root, 5)
        self.assertIsNone(result)

    def test_node_in_left_subtree(self):
        root = create_tree([4, 2, 7, 1, 3])
        result = self.sol.searchBST(root, 1)
        self.assertEqual(result.val, 1)

    def test_node_in_right_subtree(self):
        root = create_tree([4, 2, 7, 1, 3])
        result = self.sol.searchBST(root, 7)
        self.assertEqual(result.val, 7)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
