from random import random
from unittest import TestCase
from tree_node_helpers import *

# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # search for node
        node = root
        parent = left = None
        while node:
            if node.val < key:
                parent, node, left = node, node.right, False
            elif node.val > key:
                parent, node, left = node, node.left, True
            else:
                break  # found

        # Delete the node with iterative in order succession
        if node:  # if found
            if not (node.left and node.right): # one or no children
                if parent:
                    if left:
                        parent.left = node.left or node.right
                    else:
                        parent.right = node.left or node.right
                else:
                    return node.left or node.right
            else:  # 2 children - in order successor
                temp = parent = node  # store node to delete
                node = node.left  # start left
                if not node.right:  # if left has no right subtree
                    parent.left = node.left # replace with left's left child
                else:  # find the rightmost node in the left subtree (in order)
                    while node.right: # traverse right until the end
                        parent, node = node, node.right
                    parent.right = node.left  # parent in successor's left child
                temp.val = node.val  # Copy successor's value to deleted node position

        # Return the root
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
        # Two possible valid results after deletion:
        # 1. Using successor:   [6, 3, 7, 2, 4]
        # 2. Using predecessor: [4, 3, 6, 2, None, None, 7]
        root = create_tree([5, 3, 6, 2, 4, None, 7])
        key = 5
        expected1 = create_tree([6, 3, 7, 2, 4])
        expected2 = create_tree([4, 3, 6, 2, None, None, 7])
        result = self.sol.deleteNode(root, key)
        self.assertTrue(trees_are_equal(result, expected1) or trees_are_equal(result, expected2))

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
