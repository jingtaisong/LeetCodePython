from unittest import (TestCase, main)
import functools

def numberOfDigit(n):
    if n == 0:
        return 1

    d = 0
    tenPower = 1
    while tenPower <= n:
        d += 1
        tenPower *= 10

    return d


def customSort(x, y):
    xNumberOfDigit = numberOfDigit(x)
    yNumberOfDigit = numberOfDigit(y)

    xComp = x * pow(10, yNumberOfDigit) + y
    yComp = y * pow(10, xNumberOfDigit) + x

    return xComp - yComp


def joinNumStr(nums):
    s = ''
    isInLeadingState = True
    for n in nums:
        if not isInLeadingState or n != 0:
            s += str(n)
            isInLeadingState = False

    if s == '':
        s = '0'

    return s


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        sortedNums = sorted(nums, key=functools.cmp_to_key(customSort), reverse=True)
        largestNumber = joinNumStr(sortedNums)
        return largestNumber

class TestLargestNumber(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [0],
            'test_ans': '0'
        }, {
            'test_nums': [0, 1],
            'test_ans': '10'
        }, {
            'test_nums': [10, 2],
            'test_ans': '210'
        }, {
            'test_nums': [3,30,34,5,9],
            'test_ans': '9534330'
        }, {
            'test_nums': [121, 12],
            'test_ans': '12121'
        }, ]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            ans = obj.largestNumber(test_case['test_nums'])
            self.assertEqual(ans, test_case['test_ans'])

if __name__ == '__main__':
    main()
