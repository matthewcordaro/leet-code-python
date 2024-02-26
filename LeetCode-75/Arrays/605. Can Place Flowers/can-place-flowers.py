from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        Constraints:
            0 <= n <= flowerbed.length
            1 <= flowerbed.length <= 2 * 104
        :param flowerbed:
        :param n:
        :return:
        """
        # Base Cases
        if n == 0:  # No plants case
            return True
        if len(flowerbed) == 1:  # Single spot case
            return flowerbed[0] == 0 and n == 1

        # Check first spot
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            if n == 1:  # We will run out of plants
                return True
            flowerbed[0], n = 1, n - 1  # Plant one

        # Check middle spots
        for i in range(1, len(flowerbed) - 1):
            if (flowerbed[i - 1] == 0
                    and flowerbed[i] == 0
                    and flowerbed[i + 1] == 0):
                if n == 1:  # We will run out of plants
                    return True
                flowerbed[i], n = 1, n - 1  # Plant one

        # Check final spot
        if (flowerbed[-1] == 0
                and flowerbed[-2] == 0
                and n == 1):  # Last plant goes in last spot
            return True

        # Run out of locations to plant
        return False


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))  # Middle Spot
        self.assertTrue(self.sol.canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1))  # First Spot
        self.assertTrue(self.sol.canPlaceFlowers(flowerbed=[1, 0, 1, 0, 0], n=1))  # Last Spot
        self.assertTrue(self.sol.canPlaceFlowers(flowerbed=[0], n=1))  # Single
        self.assertTrue(self.sol.canPlaceFlowers(flowerbed=[1, 0, 1, 0, 1, 0, 1], n=0))  # Zero plants
        self.assertFalse(self.sol.canPlaceFlowers(flowerbed=[1], n=1))
        self.assertFalse(self.sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
        self.assertFalse(self.sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
