from unittest import (TestCase, main)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        if N == 0:
            return ''

        palindromPosList = set()
        longestPalindrom = ''

        for pos in reversed(range(0, N)):
            char = s[pos]
            thisPalindromPosList = {1}
            # i \in thisPalindromPosList iff [pos, pos + i) is a palindrom; 1 is always in
            for i in range(2, N - pos + 1):
                if i == 2:
                    if char == s[pos + i - 1]:
                        thisPalindromPosList.add(i)
                elif ((i - 2) in palindromPosList) and char == s[pos + i - 1]:
                    thisPalindromPosList.add(i)
            thisLongestPalindromLength = max(thisPalindromPosList)
            if len(longestPalindrom) < thisLongestPalindromLength:
                longestPalindrom = s[pos: pos + thisLongestPalindromLength]
            palindromPosList = thisPalindromPosList

        return longestPalindrom

class TestLongestPalindromSubString(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_s': '',
        'test_output': '',
    }, {
        'test_s': 'a',
        'test_output': 'a',
    }, {
        'test_s': 'ab',
        'test_output': 'b',
    }, {
        'test_s': 'aba',
        'test_output': 'aba',
    }, {
        'test_s': 'babad',
        'test_output': 'aba',
    }, {
        'test_s': 'cbbd',
        'test_output': 'bb',
    }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            answer = obj.longestPalindrome(test_case['test_s'])
            expected = test_case['test_output']

            self.assertEqual(answer, expected)

if __name__ == '__main__':
    main()

