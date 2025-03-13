import heapq
from unittest import TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # noinspection PyMethodMayBeStatic
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        head = tail = ListNode()
        candidates = []
        for list_node in lists:
            if list_node and list_node is not []:
                heapq.heappush(candidates, (list_node.val, id(list_node), list_node))
        while len(candidates) > 0:
            _, _, node = candidates[0]
            if node.next is not None:
                heapq.heapreplace(candidates, (node.next.val, id(node.next), node.next))
            else:
                heapq.heappop(candidates)
            tail.next = tail = node  # order matters
        return head.next


class TestSolution(TestCase):
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
    super(TestSolution())


if __name__ == '__main__':
    main()
