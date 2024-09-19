from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def majorityElement(self, nums: list[int]) -> int:
        lead = 0
        leading_candidate = None
        for num in nums:
            leading_candidate = num if lead == 0 else leading_candidate  # while they are equal, this allows for swap
            lead += 1 if num == leading_candidate else -1  # either the lead increases or decreases
        return leading_candidate


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(3, self.sol.majorityElement(nums = [3,2,3]))
        self.assertEqual(2, self.sol.majorityElement(nums = [2,2,1,1,1,2,2]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
