from typing import Optional
from unittest import TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O()
class Solution:
  # noinspection PyMethodMayBeStatic
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    mid = head
    while head and head.next:
      mid = mid.next
      head = head.next.next
    return mid


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    # self.assertEqual(0, self.sol.middleNode())
    pass

def main():
    super(TestSolution())


if __name__ == '__main__':
  main()
