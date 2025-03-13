from unittest import TestCase


# O()
class Solution:
    def isNStraightHand(self, hand: [int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        groups: [[int]] = []
        for card in hand:
            groups = self.putCardIntoGroups(card, groups, groupSize)
        return all([len(group) == groupSize for group in groups])

    # noinspection PyMethodMayBeStatic
    def putCardIntoGroups(self, card: int, groups: [[int]], groupSize: int) -> [[int]]:
        full_group = None
        for group in groups:
            # Check if last card matches
            if group[-1] == card - 1:
                if len(group) == groupSize - 1:
                    full_group = group
                    break
                group.append(card)
                break
        if full_group:
            groups.remove(full_group)
        return groups


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
        self.assertFalse(self.sol.isNStraightHand(hand=[8, 10, 12], groupSize=3))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
