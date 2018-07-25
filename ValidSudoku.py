from unittest import (TestCase, main)


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # x (resp. y): the occurance of x(resp. y)-coordinates, block: the occurance of (x // 3) * 3 + (y // 3)
        occuranceList = dict()

        for i in range(1, 10):
            occuranceList[str(i)] = dict({'x': set(), 'y': set(), 'block': set()})

        for x in range(0, 9):
            for y in range(0, 9):
                element = board[x][y]
                if element != '.':
                    if (x in occuranceList[element]['x']) or (y in occuranceList[element]['y']) or ( ((x // 3) * 3 + (y // 3)) in occuranceList[element]['block']):
                        return False
                    else:
                        occuranceList[element]['x'].add(x)
                        occuranceList[element]['y'].add(y)
                        occuranceList[element]['block'].add((x // 3) * 3 + (y // 3))

        return True


class TestValidSoduku(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_board': [
              ["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ],
            'test_ans': True
        }, {
            'test_board': [
              ["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ],
            'test_ans': False
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            ans = obj.isValidSudoku(test_case['test_board'])
            self.assertEqual(ans, test_case['test_ans'])

if __name__ == '__main__':
    main()
