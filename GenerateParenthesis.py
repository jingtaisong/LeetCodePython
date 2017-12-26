from unittest import (TestCase, main)

import collections

class GenerateParenthesis(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        levels = collections.deque()
        levels.append([1])

        parentheses = []

        while len(levels):
            currentLevel = levels.popleft()
            currentLength = len(currentLevel)
            lastLevel = currentLevel[-1]
            if currentLength == 2 * n:
                currentParentheses = []
                prevLevel = 0
                for thisLevel in currentLevel:
                    if thisLevel == prevLevel + 1:
                        currentParentheses.append("(")
                    else:
                        currentParentheses.append(")")
                    prevLevel = thisLevel
                parentheses.append("".join(currentParentheses))
            else:
                if lastLevel + currentLength < 2 * n:
                    newLevel = [x for x in currentLevel]
                    newLevel.append(lastLevel + 1)
                    levels.append(newLevel)

                if lastLevel > 0:
                    newLevel = [x for x in currentLevel]
                    newLevel.append(lastLevel - 1)
                    levels.append(newLevel)

        return parentheses


class TestGenerateParenthesis(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_n': 3,
        'test_output': [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
    }]

    def test_result(self):
        obj = GenerateParenthesis()

        for test_case in self.test_object:
            answer = obj.generateParenthesis(test_case['test_n'])

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

