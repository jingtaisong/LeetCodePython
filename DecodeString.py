from unittest import (TestCase, main)

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()
        recentNumberString = ""
        recentLetterString = ""

        for c in s:
            if c.isdigit():
                recentNumberString += c
            elif c.isalpha():
                recentLetterString += c
            elif c == "[":
                stack.append(recentLetterString)
                recentNumber = int(recentNumberString)
                stack.append(recentNumber)
                recentNumberString = ""
                recentLetterString = ""
            elif c == "]":
                recentNumber = stack.pop()
                prevLetterString = stack.pop()
                recentLetterString = prevLetterString + recentLetterString * recentNumber
            else:
                raise ValueError('Did not expect character {ch}!'.format(ch=c))

        return recentLetterString


class TestDecodeString(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_s': '2[2[y]pq4[2[jk]e1[f]]]ef',
            'answer': 'yypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
        }, {
            'test_s': '2[2[a]b1[c]]',
            'answer': 'aabcaabc',
        }, {
            'test_s': '3[a]2[b4[F]c]',
            'answer': 'aaabFFFFcbFFFFc',
        }, {
            'test_s': '',
            'answer': '',
        }, {
            'test_s': 'a',
            'answer': 'a',
        }, {
            'test_s': 'ab',
            'answer': 'ab',
        }, {
            'test_s': '2[a]',
            'answer': 'aa',
        }, {
            'test_s': '10[a]',
            'answer': 'aaaaaaaaaa',
        }, {
            'test_s': '2[ab]',
            'answer': 'abab',
        }, {
            'test_s': '2[ab]cd',
            'answer': 'ababcd',
        }, {
            'test_s': '2[a2[b]c]',
            'answer': 'abbcabbc',
        }, {
            'test_s': '2[a2[b]c2[d]]',
            'answer': 'abbcddabbcdd',
        }, {
            'test_s': '2[a]3[b]',
            'answer': 'aabbb',
        }, {
            'test_s': '2[abc]3[cd]ef',
            'answer': 'abcabccdcdcdef',
        }, {
            'test_s': '3[a2[c]]',
            'answer': 'accaccacc',
        }, {
            'test_s': '3[a]2[bc]',
            'answer': 'aaabcbc',
        }, {
            'test_s': '2[a2[b]]',
            'answer': 'abbabb',
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.decodeString(test_case['test_s'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
