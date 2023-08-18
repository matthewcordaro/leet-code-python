from typing import Optional
from unittest import TestCase


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MinStack:
    def __init__(self):
        self.stack: Optional[ListNode] = None
        self.minStack: Optional[ListNode] = None

    def push(self, val: int) -> None:
        # Keep a min stack with the main stack
        if not self.minStack or val <= self.minStack.value:
            new_min = ListNode(val)
            new_min.next = self.minStack
            self.minStack = new_min

        # Main Stack
        new_head = ListNode(val)
        new_head.next = self.stack
        self.stack = new_head

    # If the values are the same, pop both from the top.
    def pop(self) -> None:
        if self.stack.value == self.minStack.value:
            self.minStack = self.minStack.next
        self.stack = self.stack.next

    def top(self) -> int:
        return self.stack.value

    def getMin(self) -> int:
        return self.minStack.value


class TestSolution(TestCase):
    def setUp(self):
        self.sol = MinStack()

    def test_solution(self):
        # self.assertEqual(0, self.sol.someFunction())
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
