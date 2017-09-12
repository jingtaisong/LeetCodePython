from unittest import (TestCase, main)


def binarySearch(array, target):
    # return a triple (True/False, index lower bound, index upper bound)
    n = len(array)

    if n == 0:
        return (False, None, None)

    low = 0
    high = n  # high > low
    recentFromTarget = 0

    while low < high:
        mid = (low + high) // 2  # guaranteed low <= mid < high
        trial = array[mid]
        if trial == target:
            return (True, mid, mid)
        elif trial < target:
            low = mid + 1
            recentFromTarget = -1
        else:
            high = mid
            recentFromTarget = 1

    if recentFromTarget == -1:
        return (False, low - 1, low)
    else:
        return (False, high - 1, high)


class search2DMatrix(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)

        if m == 0:
            return False

        n = len(matrix[0])

        if n == 0:
            return False

        firstCol = [matrix[x][0] for x in range(0, m)]
        (findInFirstCol, rowLowerBound, rowUpperBound) = binarySearch(firstCol, target)
        if findInFirstCol:
            return True

        if rowLowerBound < 0:  # meaning the most upper left entry is also smaller than target
            return False

        (findInRow, colLowerBound, colUpperBound) = binarySearch(matrix[rowLowerBound], target)

        return findInRow

class TestSearch2DMatrix(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_matrix': [
             [ 1, 2, 0 ],
            ],
            'test_target': 2,
            'test_output': True
        }, {
            'test_matrix': [
             [ 1, 2, 3 ],
            ],
            'test_target': 4,
            'test_output': False
        }, {
            'test_matrix': [
             [ 1, 2, 3 ],
            ],
            'test_target': 0,
            'test_output': False
        }, {
            'test_matrix': [
             [ 1, 2, 3 ],
            ],
            'test_target': 2.5,
            'test_output': False
        }, {
            'test_matrix': [
              [1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]
            ],
            'test_target': 3,
            'test_output': True,
        }, {
            'test_matrix': [
              [1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]
            ],
            'test_target': 12,
            'test_output': False,
        }, {
            'test_matrix': [
              [1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]
            ],
            'test_target': 11,
            'test_output': True,
        }, {
            'test_matrix': [
              [1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]
            ],
            'test_target': 50,
            'test_output': True,
        }, {
            'test_matrix': [
              [1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]
            ],
            'test_target': 51,
            'test_output': False,
        }]

    def test_result(self):
        obj = search2DMatrix()

        for test_case in self.test_object:
            result = obj.searchMatrix(test_case['test_matrix'], test_case['test_target'])

            self.assertEqual(result, test_case['test_output'])

if __name__ == '__main__':
    main()