from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Helper function to create a binary tree from a list of values in level-order.
    Args:
        vals (List[Optional[int]]): A list of values in level-order where None represents an empty node.

    Returns:
        TreeNode: The root of the binary search tree created.
    """
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

def trees_are_equal(node1: TreeNode, node2: TreeNode) -> bool:
    """
    Helper function to compare two binary trees for equality.
    """
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return (
            node1.val == node2.val
            and trees_are_equal(node1.left, node2.left)
            and trees_are_equal(node1.right, node2.right)
    )
