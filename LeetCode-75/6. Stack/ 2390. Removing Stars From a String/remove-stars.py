from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            # stack = stack[:-1] if c == '*' else stack + [c]
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("lecoe", self.sol.removeStars(s="leet**cod*e"))
        self.assertEqual("", self.sol.removeStars(s="erase*****"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
