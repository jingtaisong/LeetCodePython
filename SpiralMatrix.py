from unittest import (TestCase, main)


class SpiralMatrix(object):
    def spiralOrderHelper(self, matrix, NW1, NW2, SE1, SE2):
        """
        (NW1, NW2) is the starting northwestern coordinate, (SE1, SE2) is the starting southeastern coordinate
        """
        if NW1 > SE1 or NW2 > SE2:
            return []

        if NW1 == SE1:
            return matrix[NW1][NW2: SE2 + 1]

        if NW2 == SE2:
            return [matrix[x][SE2] for x in range(NW1, SE1 + 1)]

        # now we may assume NW1 < SE1 and NW2 < SE2
        rightward = matrix[NW1][NW2: SE2 + 1]
        downward = [matrix[x][SE2] for x in range(NW1 + 1, SE1 + 1)]
        leftward = [matrix[SE1][x] for x in range(SE2 - 1, NW2 - 1, -1)]
        upward = [matrix[x][NW2] for x in range(SE1 - 1, NW1, -1)]
        return rightward + downward + leftward + upward + self.spiralOrderHelper(matrix, NW1 + 1, NW2 + 1, SE1 - 1, SE2 - 1)


    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        numRows = len(matrix)

        if numRows == 0:
            return []

        numCols = len(matrix[0])

        if numCols == 0:
            return []

        return self.spiralOrderHelper(matrix, 0, 0, numRows - 1, numCols - 1)

class TestSpiralMatrix(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_matrix': [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
            ],
            'test_output': [1,2,3,6,9,8,7,4,5]
        }, {
            'test_matrix': [],
            'test_output': [],
        }, {
            'test_matrix': [[],[]],
            'test_output': [],
        }, {
            'test_matrix': [[1],[2]],
            'test_output': [1,2],
        }, {
            'test_matrix': [[1,2]],
            'test_output': [1,2],
        }]

    def test_result(self):
        obj = SpiralMatrix()

        for test_case in self.test_object:
            output = obj.spiralOrder(test_case['test_matrix'])

            self.assertEqual(output, test_case['test_output'])

if __name__ == '__main__':
    main()