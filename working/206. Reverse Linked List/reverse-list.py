import unittest
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n)
# There is probably better way with memory updating the pointers backwards
# But this is best for computation.
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    r: Optional[ListNode] = None
    while head is not None:
      r = ListNode(head.val, r)
      head = head.next
    return r


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    pass


def main():
    unittest.main()


if __name__ == '__main__':
  main()
