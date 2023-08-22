class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n) - Memory: O(1)  Floyd's Algo
class Solution:
    # noinspection PyMethodMayBeStatic
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        turtle = rabbit = head
        while rabbit and rabbit.next:
            turtle, rabbit = turtle.next, rabbit.next.next  # Move by 1 and 2 respectively
            if turtle == rabbit:  # A cycle exists
                turtle = head  # reset
                while rabbit != turtle:
                    turtle, rabbit = turtle.next, rabbit.next
                return turtle
        return None  # No Cycle
