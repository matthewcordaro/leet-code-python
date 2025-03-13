from unittest import TestCase


# O()
class Solution:
    # noinspection PyMethodMayBeStatic
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        solution = {}
        for string in strs:
            sid = tuple(sorted(string))
            if sid in solution.keys():
                solution[sid].append(string)
            else:
                solution[sid] = [string]
        return list(solution.values())


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([''], self.sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
