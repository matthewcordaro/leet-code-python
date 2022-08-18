from typing import List


# O(n^2)
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    sublist = [target - num for num in nums]
    for i, number in enumerate(nums):
      for j, sub_number in enumerate(sublist[i + 1:]):
        if number == sub_number:
          return [i, i + j + 1]


# HashMap O(n)
class Solution2:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_dictionary = {}
    for i, number in enumerate(nums):
      if number in hash_dictionary.keys():
        return [i, hash_dictionary[number]]
      hash_dictionary[target - number] = i


if __name__ == '__main__':
  a = Solution()
  print(a.twoSum([1, 2, 3, 4, 5, 6], 4))

  a = Solution2()
  print(a.twoSum([1, 2, 3, 4, 5, 6], 4))
