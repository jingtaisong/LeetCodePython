from unittest import (TestCase, main)

def updateRunningAns(runningAns, activeNum, shouldTimeActiveNum):
    if shouldTimeActiveNum:
        runningAns *= activeNum
    else:
        runningAns = runningAns // activeNum

    return runningAns

def calculateTimeDivideOnlyAns(s, index):
    """
    :type s: str
    :rtype tuple
    return the answer from index up to the next + or - or space and the next index
    """
    n = len(s)

    digitList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if s[index] not in digitList:
        raise ValueError(
            'should have the index element a digit! But having index {ind} in string {str}, which is {ele}'.format(ind = index, str=s, ele=s[index]))

    runningAns = 1
    activeNum = 0
    movingIndex = index
    element = s[movingIndex]
    shouldTimeActiveNum = True

    while movingIndex < n:
        element = s[movingIndex]
        if element == '+' or element == '-':
            runningAns = updateRunningAns(runningAns, activeNum, shouldTimeActiveNum)
            break
        elif element == '*' or element == '/':
            # should absorb active number into running answer and reset active number
            runningAns = updateRunningAns(runningAns, activeNum, shouldTimeActiveNum)

            activeNum = 0
            shouldTimeActiveNum = element == '*'
        elif element != ' ':
            activeNum *= 10
            activeNum += int(element)

        movingIndex += 1

    if movingIndex == n:
        runningAns = updateRunningAns(runningAns, activeNum, shouldTimeActiveNum)

    return (runningAns, movingIndex)


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        index = 0
        runningAns = 0
        multiplier = 1

        while index < n:
            thisChar = s[index]
            if thisChar == ' ':
                index += 1
            elif thisChar == '+':
                multiplier = 1
                index += 1
            elif thisChar == '-':
                multiplier = -1
                index += 1
            elif thisChar == '*' or thisChar == '/':
                raise ValueError('should not expect this character to be * or /, but found {val} at index {ind}'.format(
                    val = thisChar, ind = index))
            else:  # now we can make sure thisChar is a digit
                timeDivideOnlyAns, nextIndex = calculateTimeDivideOnlyAns(s, index)
                runningAns += multiplier * timeDivideOnlyAns
                index = nextIndex

        return runningAns

class TestBasicCalculatorII(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [
        {
            'test_string': ' 3/2 ',
            'test_output': 1
        },
        {
            'test_string': '3',
            'test_output': 3
        }, {
            'test_string': '3+3*2',
            'test_output': 9
        }, {
            'test_string': ' ',
            'test_output': 0
        }, {
            'test_string': ' 3+9 / 2 ',
            'test_output': 7
        }, {
            'test_string': ' 3+19 / 2 ',
            'test_output': 12
        }, {
            'test_string': '1-1+1',
            'test_output': 1
        }]

    def test_result(self):
        obj = Solution()

        for test_case in self.test_object:
            str = test_case['test_string']
            answer = obj.calculate(str)

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()