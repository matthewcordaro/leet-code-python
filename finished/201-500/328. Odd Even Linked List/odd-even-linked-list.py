from typing import Optional
from unittest import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd, even = ListNode(), ListNode()  # dead heads for simplicity in logic
        odd_tail, even_tail = odd, even
        odd_node = True

        while head:
            if odd_node:
                odd_tail.next = head
                odd_tail = head
            else:
                even_tail.next = head
                even_tail = head
            head = head.next
            odd_node = not odd_node

        odd_tail.next = even.next  # remove the even dead head
        even_tail.next = None
        return odd.next  # remove the odd dead head


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def list_to_linked_list(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

    def test_solution(self):
        # Test with standard case
        head = self.list_to_linked_list([1, 2, 3, 4, 5])
        result = self.sol.oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 3, 5, 2, 4])

        # Test with values not matching indices
        head = self.list_to_linked_list([2, 1, 4, 3])
        result = self.sol.oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(result), [2, 4, 1, 3])

        # Test with single node
        head = self.list_to_linked_list([1])
        result = self.sol.oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(result), [1])

        # Test with empty list
        head = self.list_to_linked_list([])
        result = self.sol.oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(result), [])

        # Test with two nodes
        head = self.list_to_linked_list([1, 2])
        result = self.sol.oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 2])

        # Test with duplicates
        head = self.list_to_linked_list([1, 1, 2, 2])
        result = self.sol.oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 1, 2])


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
