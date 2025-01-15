from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def hIndex2(self, citations: list[int]) -> int:
        num_papers_checked = 0
        min_num_citations = 1001
        citations.sort(reverse=True)
        while num_papers_checked < len(citations) \
                and min_num_citations >= citations[num_papers_checked] > num_papers_checked \
                and citations[num_papers_checked] > 0:  # edge case
            min_num_citations = citations[num_papers_checked]
            num_papers_checked += 1
        return num_papers_checked


    # noinspection PyMethodMayBeStatic
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)

        for idx, paper in enumerate(citations):
            if n - idx > paper:
                return n - idx
        return 0

class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(1, self.sol.hIndex(citations=[100]))
        self.assertEqual(1, self.sol.hIndex(citations=[1, 3, 1]))
        self.assertEqual(3, self.sol.hIndex(citations=[3, 0, 6, 1, 5]))
        self.assertEqual(2, self.sol.hIndex(citations=[4, 4, 0, 0]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
