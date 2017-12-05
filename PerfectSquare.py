from unittest import (TestCase, main)

class PerfectSquare(object):
    def numSquares(self, n):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        BFS: consider a graph of positions, an edge is a word in dictionary, the existence of a path from a to b means a word of s[a:b] in the dictionary
        """
        numSquaresDP = [0]
        for i in range(1, n + 1):
            subtractee = 1
            numSquaresI = i
            while i >= subtractee * subtractee:
                numSquaresI = min(numSquaresI, numSquaresDP[i - subtractee * subtractee] + 1)
                subtractee += 1
            numSquaresDP.append(numSquaresI)

        return numSquaresDP[n]

class TestPerfectSquare(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_n': 3,
        'test_output': 3,
    }, {
        'test_n': 12,
        'test_output': 3,
    }, {
        'test_n': 13,
        'test_output': 2,
    }]

    def test_result(self):
        obj = PerfectSquare()

        for test_case in self.test_object:
            answer = obj.numSquares(test_case['test_n'])

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

