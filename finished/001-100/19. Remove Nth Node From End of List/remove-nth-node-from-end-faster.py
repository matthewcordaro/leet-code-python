import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n+m)
class Solution:
    # noinspection PyMethodMayBeStatic
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rabbit = turtle = head

        while (n := n - 1) >= 0:
            rabbit = rabbit.next

        # Edge Case: n == length of list
        if not rabbit:
            return head.next

        while rabbit := rabbit.next:
            turtle = turtle.next

        turtle.next = turtle.next.next
        return head


# class TestSolution(unittest.TestCase):
#   def setUp(self):
#     self.sol = Solution()
#
#   def test_solution(self):
#     self.assertEqual(LL([1,2,3,5]), self.sol.removeNthFromEnd(LL([1,2,3,4,5]), 2))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
