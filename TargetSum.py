from unittest import (TestCase, main)


class Solution2(object):
    def findTargetSumWaysInternal(self, nums, S, totalSum, startIndex):
        if startIndex >= len(nums):
            return S == 0
        elif totalSum < S or -totalSum > S:
            return 0
        else:
            element = nums[startIndex]
            totalSum -= element
            startIndex += 1
            lastPositiveWays = self.findTargetSumWaysInternal(nums, S - element, totalSum, startIndex)
            lastNegativeWays = self.findTargetSumWaysInternal(nums, S + element, totalSum, startIndex)
            return lastPositiveWays + lastNegativeWays

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        totalSum = sum(nums)
        return self.findTargetSumWaysInternal(nums, S, totalSum, 0)


class Solution3(object):
    def findTargetSumWaysSubset(self, nums, startIndex, SS):
        if SS < 0:
            return 0
        elif startIndex >= len(nums):
            return int(SS == 0)
        else:
            element = nums[startIndex]
            startIndex += 1

            if element > SS:
                return int(SS == 0)

            waysIncludeStart = self.findTargetSumWaysSubset(nums, startIndex, SS - element)
            waysExcludeStart = self.findTargetSumWaysSubset(nums, startIndex, SS)
            return waysIncludeStart + waysExcludeStart

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        totalSum = sum(nums)
        # equivalent to the number of subsets that add up to (totalSum + S) / 2
        if (totalSum + S) % 2 != 0 or totalSum < S:
            return 0
        SS = (totalSum + S) / 2

        # sort the list so that we know to stop once seeing an element exceed the targetSum
        nums = sorted(nums)
        return self.findTargetSumWaysSubset(nums, 0, SS)

class Solution(object):
   def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        totalSum = sum(nums)
        sumWays = dict()
        sumWays[0] = 1

        for element in nums:
            newSumWays = dict()
            for key, value in sumWays.items():
                newSumWays[key + element] = newSumWays.get(key + element, 0) + value
                newSumWays[key - element] = newSumWays.get(key - element, 0) + value
            sumWays = newSumWays

        return sumWays.get(S,0)


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [],
            'test_S': 0,
            'answer': 1
        }, {
            'test_nums': [],
            'test_S': 1,
            'answer': 0
        }, {
            'test_nums': [1],
            'test_S': 0,
            'answer': 0
        }, {
            'test_nums': [1,1],
            'test_S': 0,
            'answer': 2
        }, {
            'test_nums': [1],
            'test_S': 1,
            'answer': 1
        }, {
            'test_nums': [1,1],
            'test_S': 1,
            'answer': 0
        }, {
            'test_nums': [1,2],
            'test_S': 1,
            'answer': 1
        }, {
            'test_nums': [1,2],
            'test_S': -1,
            'answer': 1
        }, {
            'test_nums': [1,2,1],
            'test_S': 0,
            'answer': 2
        }, {
            'test_nums': [1,1,1,1,1],
            'test_S': 3,
            'answer': 5
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.findTargetSumWays(test_case['test_nums'], test_case['test_S'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
