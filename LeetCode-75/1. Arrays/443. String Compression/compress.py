from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 1:
            return 1

        # Init
        left_idx, right_idx = 0, 1
        count = 1

        def write_count():
            nonlocal left_idx, right_idx, count
            left_idx += 1  # move to writing location
            if count != 1:
                for nc in str(count):  # write every char of the number
                    chars[left_idx] = nc
                    left_idx += 1

        while right_idx < len(chars):
            if chars[left_idx] == chars[right_idx]:
                count += 1
            else:  # Write & set next
                write_count()
                chars[left_idx] = chars[right_idx]
                count = 1
            right_idx += 1

        write_count()
        chars = chars[:left_idx]  # delete from left_idx onward
        return len(chars)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(9, self.sol.compress(
            ["a", "a", "a", "b", "c", "d", "d", "d", "d", "d", "e", "f", "f"]))
        self.assertEqual(8, self.sol.compress(
            ["a", "a", "a", "b", "c", "d", "d", "d", "d", "d", "e", "f"]))
        self.assertEqual(4, self.sol.compress(
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
