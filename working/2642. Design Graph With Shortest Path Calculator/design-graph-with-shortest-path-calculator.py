import sys
from unittest import TestCase


class Node:
    def __init__(self, number: int, num_edges: int):
        self.number = number
        self.to_node_cost = [None] * num_edges


# O()
class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        # initialize nodes
        self.nodes = [Node(i, n) for i in range(n)]
        # add all edges
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: list[int]) -> None:
        (from_node, to_node, edgeCost) = edge
        self.nodes[from_node].to_node_cost[to_node] = edgeCost

    def shortestPath(self, node1: int, node2: int) -> int:
        # returns the minimum cost of a path from node1 to node2
        min_distances = [sys.maxsize] * len(self.nodes)
        current_distance = 0

        def depth_first_search(node: Node) -> None:
            min_distances[node] = min(min_distances[node], current_distance)



        depth_first_search(self.nodes[node1])
        return min_distances[node2]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(0, self.sol.someFunction())


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
