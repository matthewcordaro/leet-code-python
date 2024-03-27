from unittest import TestCase


# O()


class Solution:
    # noinspection PyMethodMayBeStatic
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:  # Resolve compression
                temp = []
                while (c := stack.pop()) != '[':
                    temp = [c] + temp
                num = ''
                while stack and (n := stack.pop()).isnumeric():
                    num = n + num
                else:  # add back if we removed too much
                    if stack:
                        stack.append(n)
                stack += int(num) * temp
        return ''.join(stack)


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual("aaabcbc", self.sol.decodeString(s="3[a]2[bc]"))
        self.assertEqual("accaccacc", self.sol.decodeString(s="3[a2[c]]"))
        self.assertEqual("abcabccdcdcdef", self.sol.decodeString(s="2[abc]3[cd]ef"))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
