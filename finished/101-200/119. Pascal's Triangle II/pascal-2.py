from unittest import TestCase


# O()
class Solution:
    def __init__(self):
        self.pascal_triangle = [[1], [1, 1]]

    def getRow(self, row_index: int) -> [int]:
        # Solution not stored? Keep building
        while row_index > len(self.pascal_triangle) - 1:
            bottom_row = self.pascal_triangle[-1]
            new_row = [1]  # Each row begins with 1
            # Calc & build row's middle
            for i in range(1, len(bottom_row)):
                new_row.append(bottom_row[i - 1] + bottom_row[i])
                i += 1
            new_row.append(1)  # Each row ends with a 1
            self.pascal_triangle.append(new_row)
        return self.pascal_triangle[row_index]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([1], self.sol.getRow(0))
        self.assertEqual([1, 1], self.sol.getRow(1))
        self.assertEqual([1, 4, 6, 4, 1], self.sol.getRow(4))
        self.assertEqual([1,
                          20,
                          190,
                          1140,
                          4845,
                          15504,
                          38760,
                          77520,
                          125970,
                          167960,
                          184756,
                          167960,
                          125970,
                          77520,
                          38760,
                          15504,
                          4845,
                          1140,
                          190,
                          20,
                          1],
                         self.sol.getRow(20))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
