from unittest import (TestCase, main)

def binarySearch(array, initLow, initHigh, target):
    if initHigh < initLow:
        raise ValueError('Initially, High {HH} is less than Low {LL}'.format(HH=initHigh, LL=initLow))
    low = initLow
    high = initHigh
    # return the least index >= target and an indicator telling whether equality holds; the answer is in [initLow, initHigh]
    while low < high:
        mid = int((low + high) / 2)
        element = array[mid]
        if element == target:
            return (mid, True)
        elif element < target:
            low = mid + 1
        else:
            high = mid
    # low must be equal to high now
    if low != high:
        raise ValueError('Finally, Low {LL} is not equal to High {HH}'.format(HH=high, LL=low))

    if high >= initHigh:
        return (initHigh, False)
    elif high < initLow:
        return (initLow, False)
    elif array[high] < target:
        return (high + 1, False)
    else:
        return (high, False)


class Solution(object):
    def searchMatrixHelper(self, matrix, L, R, U, D, target):
        """
        search in a submatrix on [L, R) \times [U, D) 
        """
        if R < L:
            raise ValueError('Right {RR} is less than Left {LL}'.format(RR=R, LL=L))

        if D < U:
            raise ValueError('Down {DD} is less than Up {UU}'.format(DD=D, UU=U))

        if R == L:
            return False

        if D == U:
            return False

        if R - L >= D - U:
            # search in the middle row in the fat case
            rowInd = int((U + D) / 2)  # rowInd is in [U, D)
            colInd, foundInCol = binarySearch(matrix[rowInd], L, R, target)  # colInd is in [L, R]
            if foundInCol:
                return True
            foundInUpperRight = self.searchMatrixHelper(matrix, colInd, R, U, rowInd, target)
            if foundInUpperRight:
                return True
            foundInLowerLeft = self.searchMatrixHelper(matrix, L, colInd, rowInd + 1, D, target)
            if foundInLowerLeft:
                return True
            return False
        else:
            # search in the middle column in the tall case
            colInd = int((R + L) / 2)  # colInd is in [L, R)
            column = [x[colInd] for x in matrix]
            rowInd, foundInRow = binarySearch(column, U, D, target)  # rowInd is in [U, D]
            if foundInRow:
                return True
            foundInUpperRight = self.searchMatrixHelper(matrix, colInd + 1, R, U, rowInd, target)
            if foundInUpperRight:
                return True
            foundInLowerLeft = self.searchMatrixHelper(matrix, L, colInd, rowInd, D, target)
            if foundInLowerLeft:
                return True
            return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        return self.searchMatrixHelper(matrix, 0, N, 0, M, target)


class TestSearchIn2DMatrix(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_matrix': [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ],
        'test_target': 20,
        'test_output': False,
    }, {
        'test_matrix': [
          [-1],
          [-1]
        ],
        'test_target': -2,
        'test_output': False,
    }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            answer = obj.searchMatrix(test_case['test_matrix'], test_case['test_target'])
            expected = test_case['test_output']

            self.assertEqual(answer, expected)

if __name__ == '__main__':
    main()

