from unittest import TestCase
import bisect


# O()
class TimeMap:
    def __init__(self):
        self.time_map: dict[str, list[(int, str)]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamp_values = self.time_map.get(key, [])
        timestamp_values.append((timestamp, value))
        self.time_map.update({key: timestamp_values})

    def get(self, key: str, timestamp: int) -> str:
        tsv: list[(int, str)] = self.time_map.get(key)
        if tsv is None:  # Empty case
            return ""
        location = bisect.bisect_left(tsv, (timestamp, ""))
        if location == len(tsv):  # Rightmost end case
            (ts, v) = tsv[location - 1]
            return v
        (ts, v) = tsv[location]
        if ts != timestamp:  # Take earlier
            if location == 0:  # Leftmost end case
                return ""
            (ts, v) = tsv[location - 1]
        return v


class TestSolution(TestCase):
    def setUp(self):
        self.tm = TimeMap()
        self.commands = None
        self.inputs = None
        self.outputs = None

    def _test_solution1(self):
        self.commands = ["TimeMap", "set", "get", "get", "set", "get", "get"]
        self.inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
        self.outputs = [None, None, "bar", "bar", None, "bar2", "bar2"]
        self.execute_tests(TestSolution._test_solution1.__name__)

    def test_solution2(self):
        self.commands = ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
        self.inputs = [[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10], ["love", 15],
                       ["love", 20],
                       ["love", 25]]
        self.outputs = [None, None, None, "", "high", "high", "low", "low"]
        self.execute_tests(TestSolution.test_solution2.__name__)

    def execute_tests(self, executor: str):
        for num, (c, i, o) in enumerate(zip(self.commands, self.inputs, self.outputs)):
            if c == "TimeMap":
                self.setUp()
            elif c == "set":
                self.tm.set(*i)
            elif c == "get":
                self.assertEqual(self.tm.get(*i), o, msg=executor + ": num == " + str(num))


def main():
    super(TestSolution())


if __name__ == '__main__':
    main()
