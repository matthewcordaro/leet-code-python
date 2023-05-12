from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n) - Memory constant
class Solution:
  # noinspection PyMethodMayBeStatic
  def hasCycle(self, head: ListNode) -> bool:
    turtle = rabbit = head  # Pointers start at the head
    while rabbit and rabbit.next:
      turtle, rabbit = turtle.next, rabbit.next.next  # Move by 1 and 2 respectively
      if turtle == rabbit: return True  # A cycle exists
    return False