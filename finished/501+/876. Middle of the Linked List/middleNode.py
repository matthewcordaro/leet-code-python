from unittest import TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        current_middle = head
        c = 0
        while head:
            if c % 2:
                current_middle = current_middle.next
            head = head.next
            c += 1
        return current_middle


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
