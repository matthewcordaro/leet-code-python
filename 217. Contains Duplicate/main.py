from typing import List


# O(n)
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    hash_dictionary = {}
    for i, number in enumerate(nums):
      if number in hash_dictionary.keys():
        return True
      hash_dictionary[number] = i
    return False


if __name__ == '__main__':
  a = Solution()
  print(a.containsDuplicate([1, 2, 3, 4, 5, 6]))
  print(a.containsDuplicate([1, 2, 3, 4, 5, 6, 6]))
