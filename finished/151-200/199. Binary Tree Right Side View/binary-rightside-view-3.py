from __future__ import annotations
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def rightSideView(root: TreeNode | None) -> [int]:
        if not root:
            return []
        solution: [int] = []
        current = root
        stack: [TreeNode | None] = []
        level = 0  # How to maintain a level when going right????
        while True:
            if current is not None:
                while len(solution) < len(stack):
                    solution.append(0)
                solution[level] = current.val
                stack.append(current)
                current = current.left
                level += 1
            elif stack:
                current = stack.pop().right
                level -= 1
            else:
                return solution


# current  = 2
# stack    = [0]
# solution = [1]
class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_solution(self):
    #   self.assertEqual(self.sol.rightSideView([]), 0)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
