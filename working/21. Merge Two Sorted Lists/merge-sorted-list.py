import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n)
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Base cases
    if list1 is None:
      return list2
    if list2 is None:
      return list1

    # both should have something set return val to the smallest head
    ret = list1
    if list1.val > list2.val:
      ret = list2

    while list1 and list2 is not None:
      if list1.val <= list2.val:
        temp = list1.next
        list1.next = list2
        list1 = temp
      else:
        temp = list2.next
        list2.next = list1
        list2 = temp

    return ret


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_solution(self):
    self.assertEqual(1, 1)


def main():
    unittest.main()


if __name__ == '__main__':
  main()
