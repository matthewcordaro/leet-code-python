from bisect import insort
from unittest import TestCase


# O()
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.numbers = sorted(nums)

    def add(self, val: int) -> int:
        insort(self.numbers, val)
        return self.numbers[-self.k]


class TestSolution(TestCase):
    def setUp(self):
        self.sol = KthLargest(3, [4, 5, 8, 2])

    def test_solution(self):
        adders = [3, 5, 10, 9, 4]
        kth_largest = [4, 5, 5, 8, 8]
        for adds, kth in zip(adders, kth_largest):
            self.assertEqual(kth, self.sol.add(adds))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
