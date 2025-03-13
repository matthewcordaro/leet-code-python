from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return head
        # Find Middle (tortoise and the hair)
        t = h = head
        while h and h.next:
            t = t.next
            h = h.next.next
        # Split Lists & Reverse 2nd
        head2 = t.next
        t.next = prev = None
        while head2:
            next_tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = next_tmp
        # Merge Lists
        a, b = head, prev
        while b:
            t_a, t_b = a.next, b.next
            a.next = b
            b.next = t_a
            a, b = t_a, t_b


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
