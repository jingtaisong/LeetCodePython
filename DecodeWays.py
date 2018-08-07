from unittest import (TestCase, main)


def isDecodable(s):
    l = len(s)
    if l != 1 and l != 2:
        return False

    if l == 2 and s[0] == '0':
        return False

    d = float(s)
    return d > 0 and d <= 26


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N == 1:
            return 0 + isDecodable(s)

        if N == 2:
            if isDecodable(s[0]) and isDecodable(s[1]):
                return 1 + isDecodable(s)
            elif isDecodable(s[0]):
                return 0 + isDecodable(s)
            else:
                return 0

        prevTwo = self.numDecodings(s[0:1])
        prev = self.numDecodings(s[0:2])
        curr = None

        for i in range(2, N):
            if s[i] == '0' and s[i-1] == '0':
                return 0
            elif s[i] == '0' and isDecodable(s[i-1:i+1]):
                curr = prevTwo
            elif s[i] == '0':
                return 0
            elif isDecodable(s[i - 1:i + 1]):
                curr = prev + prevTwo
            else:
                curr = prev
            prevTwo = prev
            prev = curr

        return curr

class TestDecodeWays(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_s': '0',
            'test_ans': 0
        }, {
            'test_s': '01',
            'test_ans': 0
        }, {
            'test_s': '10',
            'test_ans': 1
        }, {
            'test_s': '12',
            'test_ans': 2
        }, {
            'test_s': '226',
            'test_ans': 3
        }, {
            'test_s': '100',
            'test_ans': 0
        }, {
            'test_s': '101',
            'test_ans': 1
        }, {
            'test_s': '110',
            'test_ans': 1
        }, {
            'test_s': '230',
            'test_ans': 0
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            ans = obj.numDecodings(test_case['test_s'])
            self.assertEqual(ans, test_case['test_ans'])

if __name__ == '__main__':
    main()
