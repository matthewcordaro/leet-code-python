import unittest
from bisect import insort
from typing import List


class KthLargest:
    # O(n log n)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.numbers = nums[-k:]

    # O(log k)
    def add(self, val: int) -> int:
        insort(self.numbers, val)
        while self.k < len(self.numbers):
            self.numbers.pop(0)
        return self.numbers[0]


class TestSolution(unittest.TestCase):
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

    def test_solution2(self):
        nums = []
        k = 1
        adders = [-3, -2, -4, 0, 4]
        solutions = [-3, -2, -2, 0, 4]
        self.sol = KthLargest(k, nums)
        i = 0
        for add, sol in zip(adders, solutions):
            response = self.sol.add(add)
            self.assertEqual(response, sol, msg="index: " + str(i))
            i += 1


def main():
    unittest.main()


if __name__ == '__main__':
    main()
