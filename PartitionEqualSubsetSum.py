from unittest import (TestCase, main)

class Solution(object):
    def hasSubsetSum(self, sortedNums, sortedNumsSum, target):
        # whether there exists a subset whose sum is equal to the target
        # assume sortedNums is sorted descending
        # use sortedNumsSum to quickly rule out cases when a few unbalancedly large elements prevents any subset to achieve the goal
        if target == 0:
            return True
        if not len(sortedNums):
            return False
        if target < 0:
            return False
        if sortedNumsSum < target:
            return False
        runningSum = 0
        for index, element in enumerate(sortedNums):
            runningSum += element
            if element == target:
                return True
            elif self.hasSubsetSum(sortedNums[index+1:], sortedNumsSum - runningSum, target - element):
                return True
        return False
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortedNums = sorted(nums, reverse=True)
        totalSum = sum(sortedNums)
        if totalSum % 2 != 0:
            return False
        return self.hasSubsetSum(sortedNums, totalSum, totalSum/2)

class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [],
            'answer': True
        }, {
            'test_nums': [1],
            'answer': False
        }, {
            'test_nums': [1,1],
            'answer': True
        }, {
            'test_nums': [2],
            'answer': False
        }, {
            'test_nums': [1,1,1],
            'answer': False
        }, {
            'test_nums': [1, 5, 11, 5],
            'answer': True
        }, {
            'test_nums': [1, 2, 3, 5],
            'answer': False
        }, {
            'test_nums': [1,2,3,4,5,6,7],
            'answer': True
        }, {
            'test_nums': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100],
            'answer': False
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.canPartition(test_case['test_nums'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
