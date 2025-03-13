from unittest import TestCase
from collections import deque


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)  # add set
            else:
                if len(stack) == 0:
                    return False  # bad length
                elif (
                        (stack[-1] == '(' and c == ')') or
                        (stack[-1] == '[' and c == ']') or
                        (stack[-1] == '{' and c == '}')
                ):
                    stack.pop()  # match
                else:
                    return False  # no match

        return len(stack) == 0


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertTrue(self.sol.isValid(""))
        self.assertTrue(self.sol.isValid("[]{}()"))
        self.assertTrue(self.sol.isValid("((()))"))
        self.assertTrue(self.sol.isValid("((({}[][]{{{}}})))"))
        self.assertTrue(self.sol.isValid("([]({}([])))"))

        self.assertFalse(self.sol.isValid("{{{{{{{)))"))
        self.assertFalse(self.sol.isValid("{"))
        self.assertFalse(self.sol.isValid("}"))
        self.assertFalse(self.sol.isValid("{{"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
