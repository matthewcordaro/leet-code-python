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
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        max_diam = 0

        def dfs(r: TreeNode | None) -> int:
            nonlocal max_diam

            # None case - 0 depth
            if not r:
                return 0

            # Get depth
            l_depth = dfs(r.left)
            r_depth = dfs(r.right)

            # check for new max
            max_diam = max(max_diam, l_depth + r_depth)

            # node case
            return 1 + max(l_depth, r_depth)

        dfs(root)
        return max_diam


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, 1)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
