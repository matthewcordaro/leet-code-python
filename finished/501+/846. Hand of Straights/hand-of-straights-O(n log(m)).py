import unittest
from collections import defaultdict
from typing import List


# O(n log(m))  n is number of cards m is number of unique cards
class Solution:
    # noinspection PyMethodMayBeStatic
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        card_piles = defaultdict(lambda: 0)
        for card in hand:
            card_piles[card] += 1
        cards = list(card_piles.keys())
        cards.sort()  # working list of available cards in order

        while len(cards) >= groupSize:  # enough cards?
            group = []
            for i in range(groupSize - 1):  # build and test a group
                if cards[i] + 1 != cards[i + 1]:
                    return False
                group.append(cards[i])
            group.append(cards[groupSize - 1])  # last card; no test needed
            for card in group:  # remove any taken
                card_piles[card] -= 1
                if card_piles[card] == 0:
                    del card_piles[card]
                    cards.remove(card)
        return len(card_piles) == 0  # True if no cards left


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        # Documentation on Python site wrong.
        # Expected: 1st argument
        # Actual:   2nd argument (items to test)
        self.assertTrue(
            self.sol.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
        self.assertFalse(self.sol.isNStraightHand(hand=[8, 10, 12], groupSize=3))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
