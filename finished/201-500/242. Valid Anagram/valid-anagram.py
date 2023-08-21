import unittest


# O(n)
class Solution:
    # noinspection PyMethodMayBeStatic
    def isAnagram(self, s: str, t: str) -> bool:
        # Basic sanity check
        if len(t) != len(s):
            return False

        # Build HashMap
        ds = {}
        for s_char in s:
            if s_char in ds.keys():
                ds[s_char] += 1
            else:
                ds[s_char] = 1

        # Compare
        for t_char in t:
            if t_char in ds.keys():
                # Too many is a fail
                if ds[t_char] == 0:
                    return False
                ds[t_char] += -1
            else:
                return False  # Unmatched

        return True  # All is good


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.a = Solution()

    def test_isAnagram(self):
        self.assertTrue(self.a.isAnagram("anagram", "ramanag"))

        self.assertFalse(self.a.isAnagram("anagram", "grandma"))
        self.assertFalse(self.a.isAnagram("anagram", "ramanagg"))
        self.assertFalse(self.a.isAnagram("anagram", "ramangg"))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
