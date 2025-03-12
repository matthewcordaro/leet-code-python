from random import random
from unittest import TestCase
from tree_node_helpers import *

# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val < key:  # Go Right
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:  # Go Left
                root.left = self.deleteNode(root.left, key)
            else:  # Found node to delete
                if not (root.left and root.right):  # Node one or no childern
                    return root.left or root.right  # Return the one or None
                node = root.right  # Lets go with the right child
                while node.left:  # find in order successor
                    node = node.left
                root.val = node.val  # replace val with the successor's val
                root.right = self.deleteNode(root.right, node.val)  # Delete the successor
        return root


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_delete_leaf_node(self):
        # Tree: [5, 3, 6, 2, 4, None, 7], Key = 7
        # Expected tree after deletion: [5, 3, 6, 2, 4]
        root = create_tree([5, 3, 6, 2, 4, None, 7])
        key = 7
        expected = create_tree([5, 3, 6, 2, 4])
        result = self.sol.deleteNode(root, key)
        self.assertTrue(trees_are_equal(result, expected))

    def test_delete_node_with_one_child(self):
        # Tree: [5, 3, 6, 2, None, None, 7], Key = 3
        # Expected tree after deletion: [5, 2, 6, None, None, None, 7]
        root = create_tree([5, 3, 6, 2, None, None, 7])
        key = 3
        expected = create_tree([5, 2, 6, None, None, None, 7])
        result = self.sol.deleteNode(root, key)
        self.assertTrue(trees_are_equal(result, expected))

    def test_delete_node_with_two_children(self):
        # Tree: [5, 3, 6, 2, 4, None, 7], Key = 5
        # Expected tree after deletion: [6, 3, 7, 2, 4]
        root = create_tree([5, 3, 6, 2, 4, None, 7])
        key = 5
        expected = create_tree([6, 3, 7, 2, 4])
        result = self.sol.deleteNode(root, key)
        self.assertTrue(trees_are_equal(result, expected))

    def test_delete_root_node(self):
        # Tree: [2, 1], Key = 2
        # Expected tree after deletion: [1]
        root = create_tree([2, 1])
        key = 2
        expected = create_tree([1])
        result = self.sol.deleteNode(root, key)
        self.assertTrue(trees_are_equal(result, expected))

    def test_delete_non_existent_node(self):
        # Tree: [5, 3, 6, 2, 4, None, 7], Key = 10
        # Expected tree after deletion: [5, 3, 6, 2, 4, None, 7] (unchanged)
        root = create_tree([5, 3, 6, 2, 4, None, 7])
        key = 10
        expected = create_tree([5, 3, 6, 2, 4, None, 7])
        result = self.sol.deleteNode(root, key)
        self.assertTrue(trees_are_equal(result, expected))

    def test_empty_tree(self):
        # Empty tree, Key = 1
        # Expected tree after deletion: None
        root = None
        key = 1
        result = self.sol.deleteNode(root, key)
        self.assertIsNone(result)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
