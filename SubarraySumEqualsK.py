from unittest import (TestCase, main)


def addDictionary(d1, d2):
    keys = set(d1) | set(d2)
    sumDict = dict()
    for k in keys:
        sumDict[k] = d1.get(k, 0) + d2.get(k, 0)
    return sumDict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(N) solution
        runningSumList = dict()  # store the running sums since index 0 util any index
        runningSumList[0] = 1
        runningSum = 0
        count = 0
        # if runningSumList has reached runningSum - k before, the complement contributes one count
        for item in nums:
            runningSum += item
            count += runningSumList.get(runningSum - k, 0)
            runningSumList[runningSum] = runningSumList.get(runningSum, 0) + 1

        return count

    def subarraySumN2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        runningSum = 0
        N = 0
        runningList = [0]
        for item in nums:
            runningSum += item
            N += 1
            runningList.append(runningSum)

        count = 0
        for i in range(0, N + 1):
            for j in range(i + 1, N + 1):
                if runningList[j] - runningList[i] == k:
                    count += 1

        return count


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [],
            'test_k': 0,
            'answer': 0
        }, {
            'test_nums': [1],
            'test_k': 1,
            'answer': 1
        }, {
            'test_nums': [1],
            'test_k': 0,
            'answer': 0
        }, {
            'test_nums': [1,1,1],
            'test_k': 2,
            'answer': 2
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.subarraySum(test_case['test_nums'], test_case['test_k'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
