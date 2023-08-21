import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n)
# The better way with memory.
class Solution:
    # noinspection PyMethodMayBeStatic
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev: Optional[ListNode] = None
        while head is not None:
            temp = head.next
            head.next = rev
            rev = head
            head = temp
        return rev


# O(n)
# There is probably better way with memory updating the pointers backwards
# But this is best for computation.
class Solution2:
    # noinspection PyMethodMayBeStatic
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
