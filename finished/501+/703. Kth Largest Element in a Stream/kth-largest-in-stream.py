from unittest import TestCase
from bisect import insort


# O()
class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        nums.sort()
        self.numbers = nums

    def add(self, val: int) -> int:
        insort(self.numbers, val)
        return self.numbers[-self.k]


class TestSolution(TestCase):
    def test_solution(self):
        nums = [4, 5, 8, 2]
        k = 3
        adders = [3, 5, 10, 9, 4]
        solutions = [4, 5, 5, 8, 8]
        self.sol = KthLargest(k, nums)
        i = 0
        for add, sol in zip(adders, solutions):
            response = self.sol.add(add)
            self.assertEqual(response, sol, msg="index: " + str(i))
            i += 1


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
