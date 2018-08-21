from unittest import (TestCase, main)


def isBoundary(i, j, m, n):
    return i == 0 or j == 0 or i == m - 1 or j == n - 1


def searchAround(i, j, m, n, searchedStack, visited, board):
    for deltaX, deltaY in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        iNew = i + deltaX
        jNew = j + deltaY
        if iNew < 0 or iNew >= m or jNew < 0 or jNew >= n or visited[iNew][jNew] is not None:
            continue
        if board[iNew][jNew] == 'O':
            searchedStack.append((iNew, jNew))
    return


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return

        n = len(board[0])

        # visited = True means this element is on a connected component that reaches boundary
        visited = []
        for i in range(0, m):
            row = []
            for j in range(0, n):
                row.append(None)
            visited.append(row)

        for i in range(0, m):
            for j in range(0, n):
                element = board[i][j]
                if element == 'X' or visited[i][j] is not None:
                    continue
                # now this is a new connected component, based on (i, j) to search around
                searchedStack = [(i, j)]
                currentComponent = set()
                confirmedComponentReachesBoundary = False  # True means we've confirmed the current connected component reaches boundary
                while len(searchedStack):
                    iCurr, jCurr = searchedStack.pop()
                    visited[iCurr][jCurr] = True # the True at this point just means we have visited this node - may be set back to False later
                    currentComponent.add((iCurr, jCurr))

                    if not confirmedComponentReachesBoundary:
                        confirmedComponentReachesBoundary = isBoundary(iCurr, jCurr, m, n)

                    searchAround(iCurr, jCurr, m, n, searchedStack, visited, board)

                # now we have traversed this connected component, we have confirmed whether the component reaches boundary, hence we can update the visitedStatus of every position on this connected component
                for iIter, jIter in currentComponent:
                    if visited[iIter][jIter] == False:
                        raise ValueError(
                            'This is not a new connected component! i = {iCoordinate}, j = {jCoordinate}'.format(
                                iCoordinate=iIter, jCoordinate=jIter))
                    elif not confirmedComponentReachesBoundary:
                        visited[iIter][jIter] = False
                        board[iIter][jIter] = 'X'
                    # when confirmedComponentReachesBoundary is True, no need to update visitedStatus since we have set the positions on this connected component to True already

class TestFlipBoard(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_board': [['O']],
            'test_ans': [['O']]
        }, {
            'test_board': [['O', 'X']],
            'test_ans': [['O', 'X']]
        }, {
            'test_board': [['X', 'O', 'X']],
            'test_ans': [['X', 'O', 'X']]
        }, {
            'test_board': [['X', 'O', 'X'], ['X', 'X', 'X']],
            'test_ans': [['X', 'O', 'X'], ['X', 'X', 'X']]
        }, {
            'test_board': [['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']],
            'test_ans': [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        }, {
            'test_board': [['O', 'O', 'O'], ['O', 'X', 'O'], ['X', 'X', 'X']],
            'test_ans': [['O', 'O', 'O'], ['O', 'X', 'O'], ['X', 'X', 'X']]
        }, {
            'test_board': [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']],
            'test_ans': [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            board = test_case['test_board']
            obj.solve(board)
            self.assertEqual(board, test_case['test_ans'])

if __name__ == '__main__':
    main()
