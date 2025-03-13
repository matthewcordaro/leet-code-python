from unittest import TestCase

MAX_NUM = 10 ** 5 + 1


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def mostFrequentEven(self, nums: list[int]) -> int:
        count = {MAX_NUM: -1}  # {2:2, 4:2, 0:1}
        most_frequent = MAX_NUM
        for num in nums:
            if num % 2 == 0:  # Even
                count[num] = count[num] + 1 if num in count else 1
                if count[num] == count[most_frequent]:
                    most_frequent = min(num, most_frequent)
                elif count[num] > count[most_frequent]:
                    most_frequent = num
        return most_frequent if most_frequent < MAX_NUM else -1


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(2, self.sol.mostFrequentEven(nums=[0, 1, 2, 2, 4, 4, 1]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
