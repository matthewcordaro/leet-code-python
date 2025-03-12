from __future__ import annotations
from unittest import TestCase
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # noinspection PyMethodMayBeStatic
    def rightSideView(self, root: TreeNode | None) -> [int]:
        if root is None: return []

        bfs_queue = deque([root])
        result = []

        # Process each level of the tree
        while bfs_queue:
            nodes_in_level = len(bfs_queue)

            # process the level left to right
            for i in range(nodes_in_level):
                node = bfs_queue.popleft()

                # Last node at the current level? Append value
                if i == nodes_in_level - 1:
                    result.append(node.val)

                # Queue in the next level's nodes
                if node.left:
                    bfs_queue.append(node.left)
                if node.right:
                    bfs_queue.append(node.right)

        return result


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_solution(self):
    #   self.assertEqual(self.sol.rightSideView([]), 0)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
