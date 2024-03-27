from collections import deque
from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def predictPartyVictory(self, senate: str) -> str:
        sq: dict[str, deque: int] = {'R': deque(), 'D': deque()}
        rank = 0
        for party in senate:
            rank += 1
            sq[party].append(rank)
        while sq['R'] and sq['D']:
            rank += 1
            if sq['R'].popleft() < sq['D'].popleft():
                sq['R'].append(rank)
            else:
                sq['D'].append(rank)
        return 'Radiant' if sq['R'] else 'Dire'


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("Radiant", self.sol.predictPartyVictory(senate="RD"))
        self.assertEqual("Dire", self.sol.predictPartyVictory(senate="RDD"))
        self.assertEqual("Dire", self.sol.predictPartyVictory(senate="DDRRR"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()