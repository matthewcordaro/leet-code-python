from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        sol = []
        for asteroid in asteroids:
            while sol and sol[-1] > 0 > asteroid:  # collisions happening
                if sol[-1] < abs(asteroid):  # new asteroid larger
                    sol.pop()  # destroy older
                    continue  # keep looping
                # at this point the new astroid is same size or smaller
                if sol[-1] == abs(asteroid):  # both are same
                    sol.pop()  # destroy older
                break  # destroy newer
            else:  # Note: while->else is not executed if a break is executed
                sol.append(asteroid)  # newer lives on
        return sol


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertListEqual([-2, -1, 1, 2], self.sol.asteroidCollision(asteroids=[-2, -1, 1, 2]))
        self.assertListEqual([], self.sol.asteroidCollision(asteroids=[8, -8]))
        self.assertListEqual([10], self.sol.asteroidCollision(asteroids=[10, 2, -5]))
        self.assertListEqual([5, 10], self.sol.asteroidCollision(asteroids=[5, 10, -5]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
