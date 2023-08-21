from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def generateParenthesis(self, n: int) -> list[str]:
        solution = []

        def depth_first_search(working_string, open_count, close_count):
            # Base Case: At the bottom of the tree; reached a solution!
            if close_count == n:
                solution.append(working_string)
                return  # BACKTRACK

            # EXPLORE: Lets take the open parentheses if we can...
            if open_count < n:
                depth_first_search(working_string + "(", open_count + 1, close_count)
                # BACKTRACK: Variables not modified; nothing to undo!

            # EXPLORE: Lets try closing if we are allowed...
            if close_count < open_count:
                depth_first_search(working_string + ")", open_count, close_count + 1)
                # BACKTRACK: Variables not modified; nothing to undo!

        # Initialize: Execute the search from the root
        depth_first_search("", 0, 0)
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        ans = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertListEqual(sorted(ans), sorted(self.sol.generateParenthesis(3)))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
