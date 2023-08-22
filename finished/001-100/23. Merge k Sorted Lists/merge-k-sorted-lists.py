from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # noinspection PyMethodMayBeStatic
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        solution: ListNode = ListNode()
        last_node_in_solution: ListNode = solution

        total_nodes = 0
        for list_list in lists:
            while list_list:
                total_nodes += 1
                list_list = list_list.next

        while total_nodes != 0:
            node_to_pop = lists[0]
            node_to_pop_index = 0
            while node_to_pop is None:  # Deal with empty list in the front
                lists[0] = lists[len(lists) - 1]
                node_to_pop = lists[0]
                lists.pop()

            # find the lowest on top
            for list_index, list_list in enumerate(lists[1:]):
                if list_list is not None and list_list.val <= node_to_pop.val:  # skip over any empty list
                    node_to_pop = list_list
                    node_to_pop_index = list_index + 1

            # Move it to the solution
            temp = lists[node_to_pop_index]
            lists[node_to_pop_index] = lists[node_to_pop_index].next
            last_node_in_solution.next = temp
            last_node_in_solution = last_node_in_solution.next
            last_node_in_solution.next = None

            total_nodes -= 1

        return solution.next  # solution is after root.


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution1(self):
        parameters = [[1, 4, 5], [1, 3, 4], [2, 6]]
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
