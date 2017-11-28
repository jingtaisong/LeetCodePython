from unittest import (TestCase, main)
import collections

class WordBreak(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        BFS: consider a graph of positions, an edge is a word in dictionary, the existence of a path from a to b means a word of s[a:b] in the dictionary
        """
        nodeList = collections.deque([0])
        visited = set()

        while len(nodeList) > 0:
            currentNode = nodeList.popleft()
            if currentNode == len(s):
                return True
            else:
                for i in range(currentNode + 1, len(s) + 1):
                    if i in visited:
                        continue
                    else:
                        word = s[currentNode:i]
                        if word in wordDict:
                            nodeList.append(i)
                            visited.add(i)

        return False

class TestWordBreak(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_s': 'ha',
        'test_dict': ['h', 'a'],
        'test_output': True,
    }, {
        'test_s': 'ha',
        'test_dict': ['h', 'b'],
        'test_output': False,
    }, {
        'test_s': 'ha',
        'test_dict': ['a', 'h'],
        'test_output': True,
    }, {
        'test_s': 'leetcode',
        'test_dict': ['leet', 'code'],
        'test_output': True,
    }, {
        'test_s': 'leetcode',
        'test_dict': ['h', 'leet', 'co', 'df', 'de'],
        'test_output': True,
    }]

    def test_result(self):
        obj = WordBreak()

        for test_case in self.test_object:
            answer = obj.wordBreak(test_case['test_s'], test_case['test_dict'])

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

