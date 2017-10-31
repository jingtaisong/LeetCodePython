from unittest import (TestCase, main)

class UniqueBinaryTree(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        calculatedNums = [1]  # f(0) := 1
        index = 0  # what have been stored in calculatedNums
        runningSum = 1

        while index < n:
            # calculatedNums should store [f(0), f(1), ..., f(n-1)]
            runningSum = 0
            # f(n) = f(0)f(n-1) + f(1)f(n-2) + ... + f(n-1)f(0)
            for subIndex in range(0, index + 1):
                runningSum += calculatedNums[subIndex] * calculatedNums[index - subIndex]

            calculatedNums.append(runningSum)
            index += 1

        return runningSum

class TestGroupAnagram(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_n': 1,
        'test_output': 1,
    }, {
        'test_n': 2,
        'test_output': 2,
    }, {
        'test_n': 3,
        'test_output': 5,
    },
        ]

    def test_result(self):
        obj = UniqueBinaryTree()

        for test_case in self.test_object:
            answer = obj.numTrees(test_case['test_n'])

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

