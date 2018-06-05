from unittest import (TestCase, main)

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store the number of palindromic strings from index i to the most recent visited index
        visitedIndex = 0
        countPalindromicUntilVisited = [1]  # since 0 until 0: 1 palindromic
        n = len(s)
        if n == 0:
            return 0

        if n == 1:
            return 1

        count = 1

        while visitedIndex < n - 1:
            visitedIndex += 1
            # now visitedIndex >= 1
            nextChar = s[visitedIndex]
            # visitedIndex -> visitedIndex must be palindromic
            countPalindromicUntilVisited.append(1)
            countUntilVisited = 1
            for i in range(0, visitedIndex):
                if s[i] == nextChar:
                    # if i = visitedIndex - 1 then we are done
                    if i == visitedIndex - 1:
                        countPalindromicUntilVisited[i] = 1
                        countUntilVisited += 1
                    else:
                        # now i <= visitedIndex - 2, i + 1 <= visitedIndex - 1
                        # whether i -> visitedIndex is palindromic depends on whether i+1 -> visitedIndex - 1 is palindromic
                        countPalindromicUntilVisited[i] = countPalindromicUntilVisited[i + 1]
                        countUntilVisited += countPalindromicUntilVisited[i]
                else:
                    countPalindromicUntilVisited[i] = 0
            count += countUntilVisited

        return count


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_s': '',
            'answer': 0
        }, {
            'test_s': 'a',
            'answer': 1
        }, {
            'test_s': 'ab',
            'answer': 2
        }, {
            'test_s': 'abc',
            'answer': 3
        }, {
            'test_s': 'aa',
            'answer': 3
        }, {
            'test_s': 'aab',
            'answer': 4
        }, {
            'test_s': 'aba',
            'answer': 4
        }, {
            'test_s': 'aaa',
            'answer': 6
        }, {
            'test_s': 'aaaa',
            'answer': 10
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.countSubstrings(test_case['test_s'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
