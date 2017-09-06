from unittest import (TestCase, main)


class SetMatrixZero(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        scan row by row; 
            when seeing a zero entry, check the entry above it, if it is zero already, then do nothing to the column; otherwise go through this column, set non zero to zero and zero below it to one (this is to distinguish an original zero from a derived zero; this helps us to keep track whether need to nullify this row and this is the sole reason to flip it to nonzero; we will flip it back to zero once we get the mark to nullify this row).
            when seeing a non zero entry, check the entry above it, if it is zero, then this entry was originally zero, set nullify this row = true and turn this entry back to zero; otherwise this entry was unmofidified and originally non zero, too, so do nothing 
        Then remember to set "nullify the prev row" equals true (default to be false). Then nullify the prev row if nullify the prev row = true. We nullify the prev row at the last to avoid polluting the prev row from telling us whether the column has been already nullified. Should have time complexity O(mn) and space complexity O(1)
        """
        numRows = len(matrix)

        if numRows == 0:
            return

        numCols = len(matrix[0])

        nullifyPrevRow = False

        for rowIndex in range(numRows):
            nullifyThisRow = False
            for colIndex in range(numCols):
                entry = matrix[rowIndex][colIndex]
                if entry == 0:
                    if rowIndex == 0 or matrix[rowIndex - 1][colIndex] != 0:  # always nullify the column if this is the first row; otherwise nullify the column if the entry above is not zero
                        nullifyThisRow = True
                        for rowCursor in range(numRows):
                            cursor = matrix[rowCursor][colIndex]
                            if cursor == 0 and rowCursor > rowIndex:
                                matrix[rowCursor][colIndex] = 1  # flip the entry to 1 if it was originally zero and sits below this entry
                            else:
                                matrix[rowCursor][colIndex] = 0
                else:
                    if rowIndex > 0 and matrix[rowIndex - 1][colIndex] == 0:
                        nullifyThisRow = True
                        matrix[rowIndex][colIndex] = 0

            # nullify the prev row if needed to
            if nullifyPrevRow and rowIndex > 0:
                for colCursor in range(numCols):
                    matrix[rowIndex - 1][colCursor] = 0
            # only nullify this row now if this is the last row
            if rowIndex == numRows - 1 and nullifyThisRow:
                for colCursor in range(numCols):
                    matrix[numRows - 1][colCursor] = 0
            # set nullifyPrevRow
            nullifyPrevRow = nullifyThisRow

class TestSetMatrixZero(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_matrix': [[ 1, 2, 0 ]],
            'test_output': [[0,0,0]]
        }, {
            'test_matrix': [[1], [0], [2]],
            'test_output': [[0], [0], [0]],
        }, {
            'test_matrix': [[1,2,3]],
            'test_output': [[1,2,3]],
        }, {
            'test_matrix': [[1],[2],[3]],
            'test_output': [[1],[2],[3]],
        }, {
            'test_matrix': [[1,2],[2,0]],
            'test_output': [[1,0],[0,0]],
        }, {
            'test_matrix': [[1,2,3],[2,0,4],[2,1,7]],
            'test_output': [[1,0,3],[0,0,0],[2,0,7]],
        }, {
            'test_matrix': [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]],
            'test_output': [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]],
        }]

    def test_result(self):
        obj = SetMatrixZero()

        for test_case in self.test_object:
            matrix = test_case['test_matrix']
            output = obj.setZeroes(matrix)

            self.assertEqual(matrix, test_case['test_output'])

if __name__ == '__main__':
    main()