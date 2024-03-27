from unittest import TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(array: list):
    if not array:
        return None
    head = ListNode(array[0])
    head.next = list_to_linked_list(array[1:])
    return head


def consume_to_list(head: ListNode):
    array = []
    while head is not None:
        array.append(head.val)
        head = head.next
    return array


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        turtle, rabbit = head, head.next.next
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
        turtle.next = turtle.next.next
        return head


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        test_linked_list = list_to_linked_list([1, 3, 4, 7, 1, 2, 6])
        test_sol = consume_to_list(self.sol.deleteMiddle(test_linked_list))
        self.assertListEqual([1, 3, 4, 1, 2, 6], test_sol)

        test_linked_list = list_to_linked_list([1, 2, 3, 4])
        test_sol = consume_to_list(self.sol.deleteMiddle(test_linked_list))
        self.assertListEqual([1, 2, 4], test_sol)

        test_linked_list = list_to_linked_list([2, 1])
        test_sol = consume_to_list(self.sol.deleteMiddle(test_linked_list))
        self.assertListEqual([2], test_sol)

        test_linked_list = list_to_linked_list([1])
        test_sol = consume_to_list(self.sol.deleteMiddle(test_linked_list))
        self.assertListEqual([], test_sol)


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
