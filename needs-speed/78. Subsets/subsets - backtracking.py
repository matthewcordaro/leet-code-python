from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    # Choices:  Either take then number or not.
    # Constraints:  None really; only take 1 or none
    # Goal: deciding on each number
    # All really the same thing.
    #
    def subsets(self, nums: list[int]) -> list[list[int]]:
        solution = []
        subset_from_path = []

        def depth_first_search(index):
            # Base Case Out Of Bounds
            if index >= len(nums):
                # Since we're at the end, we've reached a goal!
                # Save a copy of the current working subset in the solution set
                solution.append(subset_from_path.copy())
                return

            # EXPLORE: Lets take the number (at index)...
            subset_from_path.append(nums[index])
            # And continue on
            depth_first_search(index + 1)

            # BACKTRACK: Remove the number we took, so we can try another path.
            subset_from_path.pop()

            # EXPLORE: Lets skip to the number...
            # And continue on
            depth_first_search(index + 1)

        # execute the search from the root
        depth_first_search(0)
        return solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        ans = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertListEqual(sorted(ans), sorted(self.sol.subsets(nums=[1, 2, 3])))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
