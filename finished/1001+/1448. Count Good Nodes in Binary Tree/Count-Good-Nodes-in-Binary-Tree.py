from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def goodNodes(self, root: TreeNode) -> int:
        total_good_nodes = 0

        def dfs(node: TreeNode, max_value: int) -> None:
            if not node:
                return
            if node.val > max_value:
                nonlocal total_good_nodes
                total_good_nodes += 1
            if node.left:
                dfs(node.left, max(max_value, node.val))
            if node.right:
                dfs(node.right, max(max_value, node.val))

        dfs(root, root.val)
        return total_good_nodes


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.someFunction())


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
