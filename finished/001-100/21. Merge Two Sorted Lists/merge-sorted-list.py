import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # returner + a pointer for help
        ret = p = ListNode()

        # merge while 2 lists exist
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
                p = p.next
            else:
                p.next = list2
                list2 = list2.next
                p = p.next

        # add the end of remaining if it exists
        if list1:
            p.next = list1
        elif list2:
            p.next = list2

        return ret.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, 1)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
