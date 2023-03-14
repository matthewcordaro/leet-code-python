from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n)
class Solution:
  # noinspection PyMethodMayBeStatic
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    c, s = 0, set()
    while head:
      s.add(head)
      if len(s) != (c:=c+1): return True
      head = head.next
    return False
