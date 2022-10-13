import unittest
import bisect
from typing import List


# O()
class TimeMap:
  def __init__(self):
    self.time_map: dict[str, TimeMap.ValueTimeStamps] = {}

  #  Stores the key "key" with the value "value" at the given time "timestamp".
  def set(self, key: str, value: str, timestamp: int) -> None:
    vts = self.time_map.get(key)
    if vts is not None:
      # add the timestamp
      return vts.add_timestamp(timestamp)
    # create first
    self.time_map.update({key: self.ValueTimeStamps(value, timestamp)})


  # Returns a value such that "set" was called previously, with "timestamp_prev <= timestamp". If there are multiple
  # such values, it returns the value associated with the largest "timestamp_prev". If there are no values, it returns
  # "".
  def get(self, key: str, timestamp: int) -> str:
    vts =  self.time_map.get(key)
    return "" if vts is None else vts.find_timestamp()

  class ValueTimeStamps:
    def __init__(self, value: str, timestamp: int):
      self.value = value
      self.timestamp = [timestamp]

    def add_timestamp(self, timestamp: int):
      bisect.insort(self.timestamp, timestamp)

    def find_timestamp(self, timestamp: int) -> int:



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.tm = TimeMap()
    self.commands = None
    self.inputs = None
    self.outputs = None

  def test_solution1(self):
    self.commands = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    self.inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    self.outputs = [None, None, "bar", "bar", None, "bar2", "bar2"]
    self.execute_tests()

  def execute_tests(self):
    for c, i, o in zip(self.commands, self.inputs, self.outputs):
      if c is "TimeMap":
        self.setUp()
      if c is "set":
        self.tm.set(*i)
      if c is "get":
        self.assertEqual(self.tm.get(*i), o)


def main():
  unittest.main()


if __name__ == '__main__':
  main()
