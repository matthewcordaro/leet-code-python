from typing import Optional
from unittest import TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not (l1 or l2): return None
    place_total = l1.val if l1 else 0
    place_total += l2.val if l2 else 0
    if place_total >= 10:  # Carry
        place_total -= 10
        if l1.next:
            l1.next.val +=1
        else:
            l1.next = ListNode(1)
    node = ListNode(place_total)
    node.next = add(l1.next if l1 else None, l2.next if l2 else None)
    return node

# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return add(l1,l2)

class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        pass


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
