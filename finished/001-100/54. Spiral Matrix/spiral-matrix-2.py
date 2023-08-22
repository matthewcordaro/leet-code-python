from unittest import TestCase


class Direction:
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if matrix is []:
            return []

        width, height = len(matrix[0]), len(matrix)
        size = width * height
        l: [int] = []
        visited = -200  # a value that matrix[i][j] can never be

        # Where to start
        y, x = (0, 0)
        direction = Direction.RIGHT  # start going right

        # Main Loop
        while len(l) < size:
            l.append(matrix[y][x])
            matrix[y][x] = visited
            if direction is Direction.RIGHT:
                x += 1
                if x is not width and not matrix[y][x] == visited:
                    continue
                x, y = x - 1, y + 1
                direction = Direction.DOWN
            elif direction is Direction.DOWN:
                y += 1
                if y is not height and not matrix[y][x] == visited:
                    continue
                x, y = x - 1, y - 1
                direction = Direction.LEFT
            elif direction is Direction.LEFT:
                x -= 1
                if x is not -1 and not matrix[y][x] == visited:
                    continue
                x, y = x + 1, y - 1
                direction = Direction.UP
            elif direction is Direction.UP:
                y -= 1
                if not matrix[y][x] == visited:
                    continue
                x, y = x + 1, y + 1
                direction = Direction.RIGHT
        return l


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], self.sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
