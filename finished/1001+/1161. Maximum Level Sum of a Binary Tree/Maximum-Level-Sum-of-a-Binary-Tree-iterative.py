from collections import deque
from math import inf
from typing import Optional
from unittest import TestCase
from tree_node_helpers import TreeNode, create_tree


# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(w) where w is the maximum width of the tree
class Solution:
    # noinspection PyMethodMayBeStatic
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return -1  # Error case
        bfs_queue = deque([root])
        current_max_level = -1
        current_max = -inf  # Use negative inf since we are trying to find max
        current_level = 0
        while bfs_queue:  # Breath first sum, return the level number
            current_level += 1  # Move up a level
            level_sum = 0  # for summing the level
            for _ in range(len(bfs_queue)):  # process all the nodes at the current level
                node = bfs_queue.popleft()  # For this given node
                level_sum += node.val   # add the val to the level's sum
                if node.left: bfs_queue.append(node.left)  # queue up it's left node
                if node.right: bfs_queue.append(node.right)  # queue up it's right node
            if level_sum > current_max:
                current_max = level_sum
                current_max_level = current_level
        return current_max_level


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # Tree: [1,7,0,7,-8,null,null]
        # Level 1 sum = 1
        # Level 2 sum = 7 + 0 = 7
        # Level 3 sum = 7 + (-8) = -1
        root = create_tree([1, 7, 0, 7, -8, None, None])
        self.assertEqual(self.sol.maxLevelSum(root), 2)


    def test_example2(self):
        # Tree: [989,null,10250,98693,-89388,null,null,null,-32127]
        root = create_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])
        self.assertEqual(self.sol.maxLevelSum(root), 2)


    def test_single_node(self):
        # Single node tree
        root = create_tree([1])
        self.assertEqual(self.sol.maxLevelSum(root), 1)


    def test_complete_binary_tree(self):
        # Complete binary tree with all positive values
        root = create_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.maxLevelSum(root), 3)  # Level 3 has sum = 4+5+6+7 = 22


    def test_negative_values(self):
        # Tree with negative values
        root = create_tree([-100, -200, -300, -20, -50, -30, -40])
        self.assertEqual(self.sol.maxLevelSum(root), 1)  # Level 1 has the "lowest negative" sum


    def test_empty_tree(self):
        # Empty tree not in problem but nice to have
        root = None
        self.assertEqual(self.sol.maxLevelSum(root), -1)


    def test_unbalanced_tree(self):
        # Unbalanced tree with left-heavy structure
        root = create_tree([1, 2, None, 3, None, None, None])
        self.assertEqual(self.sol.maxLevelSum(root), 3)

def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
