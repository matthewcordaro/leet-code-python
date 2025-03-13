from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n)
# The better way with memory.
class Solution:
    # noinspection PyMethodMayBeStatic
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        rev: ListNode | None = None
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
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        r: ListNode | None = None
        while head is not None:
            r = ListNode(head.val, r)
            head = head.next
        return r


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
