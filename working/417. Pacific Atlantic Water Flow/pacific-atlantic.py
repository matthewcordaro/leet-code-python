from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        num_rows, num_cols = len(heights), len(heights[0])
        # Starting points along the shore (edges)
        atlantic = {(num_rows - 1, c) for c in range(num_cols)} | {(r, num_cols - 1) for r in range(num_rows)}
        pacific = {(0, c) for c in range(num_cols)} | {(r, 0) for r in range(num_rows)}

        def search_out_from(visited: set[tuple[int, int]]) -> None:
            search_cells = visited.copy()
            while len(search_cells) > 0:
                sources_found_this_iteration: list[tuple[int, int]] = []
                for sink_row, sink_col in search_cells:
                    for potential_source in ((sink_row, sink_col - 1),
                                             (sink_row, sink_col + 1),
                                             (sink_row - 1, sink_col),
                                             (sink_row + 1, sink_col)):
                        potential_source_row, potential_source_col = potential_source
                        if potential_source not in visited \
                                and 0 <= potential_source_row < num_rows and 0 <= potential_source_col < num_cols \
                                and heights[potential_source_row][potential_source_col] >= heights[sink_row][sink_col]:
                            sources_found_this_iteration.append(potential_source)
                            visited.add(potential_source)
                search_cells = sources_found_this_iteration
            return

        # Solution
        search_out_from(atlantic)
        search_out_from(pacific)
        return [[r, c] for r, c in atlantic & pacific]  # convert for linter well-being


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        def convert_ll_to_st(lol: list[list[int, int]]) -> set[tuple[int, int]]:
            return {(x, y) for x, y in lol}

        # Test A
        expected = convert_ll_to_st([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
        actual = convert_ll_to_st(self.sol.pacificAtlantic(
            heights=[[1, 2, 2, 3, 5],
                     [3, 2, 3, 4, 4],
                     [2, 4, 5, 3, 1],
                     [6, 7, 1, 4, 5],
                     [5, 1, 1, 2, 4]]))
        self.assertSetEqual(expected, actual, f'\n\nexpected: {expected} \nbut got:  {actual}')

        # TestB
        self.assertEqual([[0, 0]], self.sol.pacificAtlantic(heights=[[1]]))

        # Test C
        expected = convert_ll_to_st([[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]])
        actual = convert_ll_to_st(self.sol.pacificAtlantic(
            heights=[[1, 1],
                     [1, 1],
                     [1, 1]]))
        self.assertSetEqual(expected, actual, f'\n\nexpected: {expected} \nbut got:  {actual}')


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
