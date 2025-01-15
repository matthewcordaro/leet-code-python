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
        ret_odd_head = odd_nodes = ListNode()
        ret_odd_head = even_nodes = ListNode()
        odd = True
        while head:
            if odd:
                odd_nodes.next = ListNode(val = head.val)

            else:
                even_nodes.val = head.val

            odd = not odd

        return ret_head


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.someFunction())


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
