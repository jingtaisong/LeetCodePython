from unittest import (TestCase, main)

def getAttempts(i, j, m, n):
    horizontalAttempts = [-1, 1]
    verticalAttempts = [-1, 1]
    if i <= 0:
        horizontalAttempts = [x for x in horizontalAttempts if x > 0]
    if i >= m - 1:
        horizontalAttempts = [x for x in horizontalAttempts if x < 0]
    if j <= 0:
        verticalAttempts = [x for x in verticalAttempts if x > 0]
    if j >= n - 1:
        verticalAttempts = [x for x in verticalAttempts if x < 0]
    attempts = []
    for h in horizontalAttempts:
        attempts.append((h, 0))
    for v in verticalAttempts:
        attempts.append((0, v))
    return attempts


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        w = len(word)
        if w == 0:
            return False

        m = len(board)
        if m == 0:
            return False

        n = len(board[0])
        if n == 0:
            return False

        pathList = []
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    pathList.append([(i, j)])

        while len(pathList):
            lastPath = pathList.pop()
            pos = len(lastPath)
            if pos == w:
                return True
            else:
                # nullify board along lastPath to avoid reusing a visited cell
                for i, j in lastPath:
                    board[i][j] = ''
                attempts = getAttempts(i, j, m, n)
                for attempt_i, attempt_j in attempts:
                    if board[i + attempt_i][j + attempt_j] == word[pos]:
                        newPath = [x for x in lastPath]
                        newPath.append((i + attempt_i, j + attempt_j))
                        pathList.append(newPath)
                # change back the visited cells
                for p in range(0, pos):
                    i, j = lastPath[p]
                    board[i][j] = word[p]

        return False

class TestLongestPalindromSubString(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        'test_word': 'ABCCED',
        'test_output': True,
    }, {
        'test_board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        'test_word': 'SEE',
        'test_output': True,
    }, {
        'test_board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        'test_word': 'ABCB',
        'test_output': False,
    }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            answer = obj.exist(test_case['test_board'], test_case['test_word'])
            expected = test_case['test_output']

            self.assertEqual(answer, expected)

if __name__ == '__main__':
    main()

