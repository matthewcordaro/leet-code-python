import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O(n)
class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    n, a, b = root.val, p.val, q.val
    # Found
    if (a <= n <= b) or (b <= n <= a): return root
    # Search to the correct side
    return self.lowestCommonAncestor(root.left, p, q) if a < n else self.lowestCommonAncestor(root.right, p, q)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(1, 1)


def main():
    unittest.main()


if __name__ == '__main__':
  main()
