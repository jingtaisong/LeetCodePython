from unittest import (TestCase, main)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        runningProdFromLeft = 1
        for i in range(0, n):
            ans.append(runningProdFromLeft)
            runningProdFromLeft *= nums[i]
        # now we have [1, a_0, a_0a_1, ..., a_0a_1...a_{n-1}]

        runningProdFromRight = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= runningProdFromRight
            runningProdFromRight *= nums[i]

        return ans


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [1,2],
            'answer': [2,1]
        }, {
            'test_nums': [1,2,3],
            'answer': [6,3,2]
        }, {
            'test_nums': [1,2,3,4],
            'answer': [24,12,8,6]
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.productExceptSelf(test_case['test_nums'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
