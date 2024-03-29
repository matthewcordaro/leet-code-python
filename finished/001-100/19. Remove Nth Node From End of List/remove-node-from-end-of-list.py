from unittest import TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(2n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next:
            return None

        count = 1
        node = head
        while node.next:
            node = node.next
            count += 1

        if count == n:  # edge case
            return head.next

        node = head
        for _ in range(1, count - n):
            node = node.next

        node.next = node.next.next
        return head


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
