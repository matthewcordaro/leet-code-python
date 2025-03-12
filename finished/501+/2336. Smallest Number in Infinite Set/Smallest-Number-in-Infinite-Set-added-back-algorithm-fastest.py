import heapq
from os import remove
from unittest import TestCase

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1  # Track the smallest number in infinite set
        self.heap = []  # Min-heap for added back numbers
        self.added_back = set()  # To prevent duplicates in heap

    def popSmallest(self) -> int:
        # O(log n) in worst case where n is number of elements in heap
        # heappop is O(log n), set.remove() is O(1)

        # If we have numbers in heap, they take priority because of invariant in addBack()
        if self.heap:
            num = heapq.heappop(self.heap)
            self.added_back.remove(num)
            return num

        # Otherwise return current number and increment
        num = self.curr
        self.curr += 1
        return num


    def addBack(self, num: int) -> None:
        # O(log n) in worst case where n is number of elements in heap
        # heappush is O(log n), set add and lookup is O(1)

        # Only add if:
        #  Number is less than current counter AND
        #  Number is not already in our added_back set
        if num < self.curr and num not in self.added_back:
            heapq.heappush(self.heap, num)
            self.added_back.add(num)

class TestSolution(TestCase):
    def setUp(self):
        """Creates a fresh SmallestInfiniteSet instance before each test"""
        self.sol = SmallestInfiniteSet()

    def test_initial_state(self):
        """Test the initial state and first few operations"""
        # First pop should always return 1
        self.assertEqual(self.sol.popSmallest(), 1)
        # Second pop should return 2
        self.assertEqual(self.sol.popSmallest(), 2)
        # Third pop should return 3
        self.assertEqual(self.sol.popSmallest(), 3)

    def test_leetcode_example_1(self):
        """Test the example from LeetCode description"""
        smallest_infinite_set = SmallestInfiniteSet()
        self.assertEqual(smallest_infinite_set.popSmallest(), 1)  # return 1
        self.assertEqual(smallest_infinite_set.popSmallest(), 2)  # return 2
        smallest_infinite_set.addBack(1)  # 1 is added back
        self.assertEqual(smallest_infinite_set.popSmallest(), 1)  # return 1
        self.assertEqual(smallest_infinite_set.popSmallest(), 3)  # return 3
        smallest_infinite_set.addBack(2)  # 2 is added back
        self.assertEqual(smallest_infinite_set.popSmallest(), 2)  # return 2
        self.assertEqual(smallest_infinite_set.popSmallest(), 4)  # return 4

    def test_add_back_operations(self):
        """Test adding back numbers in different scenarios"""
        # Remove first three numbers
        self.assertEqual(self.sol.popSmallest(), 1)
        self.assertEqual(self.sol.popSmallest(), 2)
        self.assertEqual(self.sol.popSmallest(), 3)

        # Add back 2
        self.sol.addBack(2)
        self.assertEqual(self.sol.popSmallest(), 2)  # Should get 2
        self.assertEqual(self.sol.popSmallest(), 4)  # Should get 4 (next available)

    def test_multiple_add_backs(self):
        """Test adding back the same number multiple times"""
        # Remove first two numbers
        self.sol.popSmallest()  # removes 1
        self.sol.popSmallest()  # removes 2

        # Add back 1 multiple times
        self.sol.addBack(1)
        self.sol.addBack(1)  # Should not affect the set
        self.sol.addBack(1)  # Should not affect the set

        # Should still get 1 only once
        self.assertEqual(self.sol.popSmallest(), 1)
        self.assertEqual(self.sol.popSmallest(), 3)  # Next available is 3

    def test_add_back_larger_numbers(self):
        """Test adding back larger numbers after several pops"""
        # Remove numbers 1 through 5
        for _ in range(5):
            self.sol.popSmallest()

        # Add back some numbers out of order
        self.sol.addBack(3)
        self.sol.addBack(1)
        self.sol.addBack(4)

        # Check if we get them in correct order
        self.assertEqual(self.sol.popSmallest(), 1)
        self.assertEqual(self.sol.popSmallest(), 3)
        self.assertEqual(self.sol.popSmallest(), 4)
        self.assertEqual(self.sol.popSmallest(), 6)  # Next available number


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
