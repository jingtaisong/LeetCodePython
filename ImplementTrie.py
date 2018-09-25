from unittest import (TestCase, main)

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.leaves = dict()
        self.markEnd = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        n = len(word)
        if n == 0:
            raise ValueError('should not expect to search an empty string!')
        else:
            leadingLetter = word[0]
            if leadingLetter in self.leaves.keys():
                if n != 1:
                    self.leaves[leadingLetter].insert(word[1:])
                else:
                    self.markEnd = True
            else:
                self.leaves[leadingLetter] = Trie()
                if n != 1:
                    self.leaves[leadingLetter].insert(word[1:])
                else:
                    self.markEnd = True

    def searchOrStartsWith(self, word, requireExact):
        """
        the wrapper on whether the word exists (requireExact = True) or starts with (requireExact = False) in the trie
        :type word: str
        :type requireExact: bool
        :rtype: bool
        """
        n = len(word)
        if n == 0:
            raise ValueError('should not expect to search an empty string!')
        else:
            leadingLetter = word[0]
            if leadingLetter in self.leaves.keys():
                if n == 1:
                    return not requireExact or self.markEnd
                else:
                    return self.leaves[leadingLetter].searchOrStartsWith(word[1:], requireExact)
            else:
                return False

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.searchOrStartsWith(word, True)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.searchOrStartsWith(prefix, False)


class TestImplementTrie(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_actions': [
                ('insert', 'a', None)
            ],
        }, {
            'test_actions': [
                ('search', 'a', False)
            ],
        }, {
            'test_actions': [
                ('startsWith', 'a', False)
            ],
        }, {
            'test_actions': [
                ('insert', 'a', None),
                ('search', 'a', True)
            ],
        }, {
            'test_actions': [
                ('insert', 'a', None),
                ('startsWith', 'a', True)
            ],
        }, {
            'test_actions': [
                ('insert', 'ab', None),
                ('search', 'a', False)
            ],
        }, {
            'test_actions': [
                ('insert', 'ab', None),
                ('startsWith', 'a', True)
            ],
        }, {
            'test_actions': [
                ('insert', 'ab', None),
                ('startsWith', 'b', False)
            ],
        }, {
            'test_actions': [
                ('insert', 'ab', None),
                ('startsWith', 'b', False),
                ('insert', 'ba', None),
                ('startsWith', 'b', True)
            ],
        }, {
            'test_actions': [
                ('insert', 'apple', None),
                ('search', 'apple', True),
                ('search', 'app', False),
                ('startsWith', 'app', True),
                ('insert', 'app', None),
                ('search', 'app', True)
            ],
        }]

    def test_result(self):
        for i, test_case in enumerate(self.test_object):
            obj = Trie()
            for action, actionTarget, actionAssertion in test_case['test_actions']:
                if action == 'insert':
                    obj.insert(actionTarget)
                elif action == 'search':
                    searchResult = obj.search(actionTarget)
                    self.assertEqual(searchResult, actionAssertion)
                else:
                    startsWithResult = obj.startsWith(actionTarget)
                    self.assertEqual(startsWithResult, actionAssertion)

if __name__ == '__main__':
    main()
