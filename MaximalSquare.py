from unittest import (TestCase, main)


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # for each i, stores the longest 1's (from left) and use the running min of left length to determine the side length of the largest square up to (i,j); advance j gradually
        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])
        if n == 0:
            return 0

        recentInfo = [0] * m
        biggestSquareLength = 0

        for j in range(0, n):
            newInfo = []

            for i in range(0, m):
                if matrix[i][j] == "1":
                    leftLength = recentInfo[i] + 1

                    runningMinLeftLength = leftLength
                    squareLength = 1

                    for squareLengthIterator in range(2, i + 2):
                        runningMinLeftLength = min(runningMinLeftLength, newInfo[i - squareLengthIterator + 1])
                        if runningMinLeftLength < squareLengthIterator:
                            break
                        else:
                            squareLength = squareLengthIterator

                else:
                    leftLength = 0
                    squareLength = 0

                biggestSquareLength = max(biggestSquareLength, squareLength)

                newInfo.append(leftLength)

            recentInfo = newInfo

        return biggestSquareLength * biggestSquareLength


class TestMaximalSquare(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_matrix': [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
        'test_output': 4
    }]

    def test_result(self):
        obj = Solution()

        for test_case in self.test_object:
            answer = obj.maximalSquare(test_case['test_matrix'])

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

