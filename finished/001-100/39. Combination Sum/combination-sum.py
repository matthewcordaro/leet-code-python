from unittest import TestCase


class Solution:
    # noinspection PyMethodMayBeStatic
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Choices:  Either keep taking same number or select the next one.
        # Constraints:  Solution can never be more than target.
        # Goal: Each solution array summation must be equal to target.

        candidates.sort()  # So we can easily reject numbers that are too big
        solution: list[list[int]] = []
        subset_from_path: list[int] = []

        def search(index, remainder):
            # GOAL? (Base Case)
            # Save a copy of the current working subset in the solution set return cause no need to continue
            if remainder == 0:
                solution.append(subset_from_path.copy())
                return

            # CONSTRAINT? (Base Case)
            # Took off too much (and we can ignore larger candidates), or we have no more candidates
            if remainder < 0 or index >= len(candidates):
                return

            # MOVE: Lets take the number (at index)
            candidate = candidates[index]
            subset_from_path.append(candidate)
            remainder -= candidate

            # EXPLORE: Repeat index
            search(index, remainder)

            # BACKTRACK: Remove the number at this index.
            remainder += subset_from_path.pop()

            # EXPLORE: And continue on
            search(index + 1, remainder)

        # START: Search from the smallest element first.
        search(0, target)
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([[2, 2, 3], [7]], self.sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
        self.assertEqual([[2, 2, 2, 2], [2, 3, 3], [3, 5]], self.sol.combinationSum(candidates=[2, 3, 5], target=8))
        self.assertEqual([], self.sol.combinationSum(candidates=[2], target=1))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
