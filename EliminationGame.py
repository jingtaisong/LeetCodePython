from unittest import (TestCase, main)

class Solution:
    def lastRemainingRightStart(self, n):
        if n == 1:
            return 1
        elif n % 2 == 0:
            return 2 * self.lastRemainingLeftStart(n / 2) - 1
        else:
            return 2 * self.lastRemainingLeftStart((n - 1) / 2)

    def lastRemainingLeftStart(self, n):
        if n == 1:
            return 1
        elif n % 2 == 0:
            return 2 * self.lastRemainingRightStart(n / 2)
        else:
            return 2 * self.lastRemainingRightStart((n - 1) / 2)

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.lastRemainingLeftStart(n)

class TestNumberOfBoomerangs(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_n': 9,
            'ans': 6
        }]

    def test_result(self):
        obj = Solution()

        for test_case in self.test_object:
            ans = obj.lastRemaining(test_case['test_n'])
            self.assertEqual(ans, test_case['ans'])

if __name__ == '__main__':
    main()
