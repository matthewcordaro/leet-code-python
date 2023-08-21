import unittest


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def compress(self, chars: list[str]) -> int:
        count = 1
        end = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
                continue
            if count > 1:
                for c in str(count):
                    chars[end] = c
                    end += 1
                count = 1
            chars[end] = chars[i]
            end += 1
        if count > 1:
            for c in str(count):
                chars[end] = c
                end += 1
        return end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        # Documentation on Python site wrong.
        # Expected: 1st argument
        # Actual:   2nd argument (items to test)
        self.assertEqual(9, self.sol.compress(
            ["a", "a", "a", "b", "c", "d", "d", "d", "d", "d", "e", "f", "f"]))

        self.assertEqual(8, self.sol.compress(
            ["a", "a", "a", "b", "c", "d", "d", "d", "d", "d", "e", "f"]))

        self.assertEqual(4, self.sol.compress(
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
