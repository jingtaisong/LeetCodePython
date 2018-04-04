from unittest import (TestCase, main)

def updateResultReducedResult(result, reducedResult):
    if reducedResult != -1:
        if result != -1:
            result = min(result, reducedResult + 1)
        else:
            result = reducedResult + 1

    return result

class Solution(object):
    def coinChangeCoinBig(self, coins, amount):
        cacheList = [-1] * (amount + 1)
        for i in range(0, amount+1):
            result = -1

            if i == 0:
                result = 0

            for c in coins:
                reducedAmount = i - c
                if reducedAmount < 0:
                    reducedResult = -1
                else:
                    reducedResult = cacheList[reducedAmount]

                result = updateResultReducedResult(result, reducedResult)

            cacheList[i] = result

        return cacheList[amount]

    def coinChangeAmountBig(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = max(coins)

        k = 0
        cacheList = []  # store the results in [(k-1)m, km)

        while k * m <= amount:
            newCacheList = []  # store the results in [km, km+b)
            newAmount = k * m
            for b in range(0, m):
                result = -1

                if k == 0 and b == 0:
                    result = 0

                # f(km+b) = min(f(km+b-c_1), f(km+b-c_2), ..., f(km_b-c_n)) + 1
                thisAmount = newAmount + b
                if thisAmount > amount:
                    break

                for c in coins:  # assume c > 1, and c <= m by our assumption on m
                    reducedAmount = thisAmount - c
                    if reducedAmount < 0:
                        reducedResult = -1
                    elif reducedAmount >= newAmount:  # reducedAmount is in [km, km+b), reduced result comes from the newCacheList
                        reducedResult = newCacheList[reducedAmount % m]
                    else:  # reducedAmount is in [(k-1)m, km), reducedResult comes from the cacheList
                        reducedResult = cacheList[reducedAmount % m]

                    result = updateResultReducedResult(result, reducedResult)

                newCacheList.append(result)

            cacheList = newCacheList
            k += 1

        # now amount is in [(k-1)m, km)
        answer = cacheList[amount % m]
        return answer

    def coinChange(self, coins, amount):
        if not len(coins):
            return -1

        # use cacheList to store results for amount N = km+b, 0<=b<m, m = Max(coins). Iterate by k
        m = max(coins)

        if m == 0 and amount > 0:
            return -1

        if m == 0 and amount == 0:
            return 0

        if m < amount:
            return self.coinChangeAmountBig(coins, amount)
        else:
            return self.coinChangeCoinBig(coins, amount)


class TestCoinChange(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_coins': [1],
            'test_amount': 1,
            'answer': 1,
        }, {
            'test_coins': [1],
            'test_amount': 2,
            'answer': 2,
        }, {
            'test_coins': [1,2],
            'test_amount': 2,
            'answer': 1,
        }, {
            'test_coins': [1,2],
            'test_amount': 1,
            'answer': 1,
        }, {
            'test_coins': [1,2],
            'test_amount': 3,
            'answer': 2,
        }, {
            'test_coins': [1,2],
            'test_amount': 4,
            'answer': 2,
        }, {
            'test_coins': [1,2],
            'test_amount': 5,
            'answer': 3,
        }, {
            'test_coins': [1,2,5],
            'test_amount': 11,
            'answer': 3,
        }, {
            'test_coins': [2],
            'test_amount': 1,
            'answer': -1,
        }, {
            'test_coins': [2],
            'test_amount': 3,
            'answer': -1,
        }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            answer = obj.coinChange(test_case['test_coins'], test_case['test_amount'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
