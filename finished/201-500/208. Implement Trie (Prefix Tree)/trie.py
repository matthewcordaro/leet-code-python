import unittest


class TrieNode:
    def __init__(self):
        self.end_count = 0
        self.children: {TrieNode} = {}

    def isEnd(self) -> bool:
        return self.end_count >= 1

    def numberOfEnds(self) -> int:
        return self.end_count


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
    Inserts the string {word} into the trie.

    :param word: String to insert
    """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]  # next
            else:
                node.children[char] = TrieNode()  # add it
                node = node.children[char]
        node.end_count += 1

    def search(self, word: str) -> bool:
        """
    Returns ``True`` if the string ``word`` is in the trie (i.e., was inserted before), and ``False`` otherwise.

    :param word: The word to search for.
    :return: True if the word is in the Trie.
    """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]  # next
            else:
                return False
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        """
    Returns ``True`` if there is a previously inserted string ``word`` that has the prefix ``prefix``, and ``False``
    otherwise.

    :param prefix: The prefix.
    :return: True if there is a previously inserted word that has the prefix.
    """
        node = self.root
        previous_node = None
        for char in prefix:
            if char in node.children:
                previous_node = node
                node = node.children[char]  # next
            else:
                return False
        return previous_node.isEnd() or self.searchForAnEnd(node)

    def searchForAnEnd(self, node: TrieNode):
        if node.isEnd():
            return True
        for char in node.children:
            if node.children[char].isEnd():
                return True
            else:
                return self.searchForAnEnd(node.children[char])
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Trie()

    def test_solution(self):
        actions = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        data = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        expected_outputs = [None, None, True, False, True, None, True]
        for i, (action, datum, expected_output) in enumerate(zip(actions, data, expected_outputs)):
            iteration = i + 1
            if action == "Trie":
                self.sol = Trie()
            if action == "insert":
                self.sol.insert(datum[0])
            if action == "search":
                self.assertEqual(expected_output, self.sol.search(datum[0]), msg="iteration # " + str(iteration))
            if action == "startsWith":
                self.assertEqual(expected_output, self.sol.startsWith(datum[0]), msg="iteration # " + str(iteration))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
