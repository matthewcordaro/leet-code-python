from typing import Optional
from unittest import TestCase
from tree_node_helpers import *


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0

        pass

def sums_in_list(lst: list[int], target: int) -> int:
    # number of subsequences that total target in lst


    pass


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        # Tree:     10
        #          /  \
        #         5   -3
        #        / \    \
        #       3   2    11
        #      / \   \
        #     3  -2   1
        # targetSum = 8
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)

        self.assertEqual(3, self.sol.pathSum(root, 8))


    def test_example_2(self):
        # Tree:     5
        #          / \
        #         4   8
        #        /   / \
        #       11  13  4
        #      /  \      \
        #     7    2      1
        # targetSum = 22
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.right.right = TreeNode(1)

        self.assertEqual(3, self.sol.pathSum(root, 22))


    def test_empty_tree(self):
        self.assertEqual(0, self.sol.pathSum(None, 1))


    def test_single_node_match(self):
        root = TreeNode(1)
        self.assertEqual(1, self.sol.pathSum(root, 1))


    def test_single_node_no_match(self):
        root = TreeNode(1)
        self.assertEqual(0, self.sol.pathSum(root, 2))


    def test_negative_values(self):
        # Tree:     1
        #          / \
        #        -2   3
        #        /     \
        #      -1      -2
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(-1)
        root.right.right = TreeNode(-2)

        self.assertEqual(2, self.sol.pathSum(root, -1))


    def test_zero_sum_path(self):
        # Tree:     1
        #          / \
        #         2  -2
        #        /     \
        #       -2      1
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(-2)
        root.left.left = TreeNode(-2)
        root.right.right = TreeNode(1)

        self.assertEqual(2, self.sol.pathSum(root, 0))

def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
