import unittest
from bisect import insort
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        ListNode.__eq__ = lambda this, other: this and other and this.val == other.val
        ListNode.__lt__ = lambda this, other: this.val < other.val

    # noinspection PyMethodMayBeStatic
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Remove any blanks
        lists = list(filter(lambda a: a is not None and a != [], lists))
        # Edge cases
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        solution: ListNode = ListNode()
        sol_tail_ptr: ListNode = solution

        lists.sort()

        while len(lists) > 1:
            # add next item to the solution
            sol_tail_ptr.next = lists[0]
            sol_tail_ptr = sol_tail_ptr.next

            # remove the first NodeList
            # if the next node exists in first NodeList, reinsert
            lists = lists[1:]
            if sol_tail_ptr.next:
                insort(lists, sol_tail_ptr.next)
            # for safety, maybe unnecessary... can speed up
            sol_tail_ptr.next = None

        # Only 1 list left now
        sol_tail_ptr.next = lists[0]
        return solution.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution1(self):
        parameters = [[1, 4, 5], [2, 6], [1, 3, 4]]
        solution = [1, 1, 2, 3, 4, 4, 5, 6]
        built_lists = [ListNode() for _ in parameters]
        for i, l_list in enumerate(parameters):
            built_lists[i] = ListNode(l_list[0])
            worker = built_lists[i]
            for item in l_list[1:]:
                worker.next = ListNode(item)
                worker = worker.next
        result = self.sol.mergeKLists(built_lists)
        i = 0
        while result:
            self.assertEqual(solution[i], result.val)
            i += 1
            result = result.next
        self.assertEqual(i, len(solution))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
