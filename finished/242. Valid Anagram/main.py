# O(n)
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    ds = {}
    # Basic sanity
    if len(t) != len(s):
      return False
    # Build HashMap
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
        # Unmatched
        return False
    return True


if __name__ == '__main__':
  a = Solution()
  # True
  print(a.isAnagram("anagram", "ramanag"))
  # False
  print(a.isAnagram("anagram", "grandma"))
  # False
  print(a.isAnagram("anagram", "ramanagg"))
  # False
  print(a.isAnagram("anagram", "ramangg"))
