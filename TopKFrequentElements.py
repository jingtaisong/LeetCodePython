from unittest import (TestCase, main)


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums = sorted(nums)
        freqList = []
        prevElement = None
        prevIndex = -1
        for index, element in enumerate(nums):
            if element != prevElement:
                if prevElement != None:
                    freqList.append({'e': prevElement, 'ct': index - prevIndex})
                prevElement = element
                prevIndex = index

        freqList.append({'e': prevElement, 'ct': len(nums) - prevIndex})

        freqList = sorted(freqList, key=lambda pair: pair['ct'], reverse=True)
        ans = [pair['e'] for i, pair in enumerate(freqList) if i < k]

        return ans


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [1],
            'test_k': 1,
            'answer': [1]
        }, {
            'test_nums': [3,0,1,0],
            'test_k': 1,
            'answer': [0]
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.topKFrequent(test_case['test_nums'], test_case['test_k'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
