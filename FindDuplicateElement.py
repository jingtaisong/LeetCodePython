from unittest import (TestCase, main)


def iterateNext(index, nums, N):
    if nums[index] >= N:
        raise ValueError('found the {i}-th element {e} in array is >= {l}'.format(i=index, e=nums[index], l=N))
    return nums[index]


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            raise ValueError('The array is empty!')

        N = len(nums)

        slow = fast = 0
        step = 0
        while step == 0 or slow != fast:
            slow = iterateNext(slow, nums, N)
            fast = iterateNext(fast, nums, N)
            fast = iterateNext(fast, nums, N)
            step += 1

        # now we know slow = fast = f^{(2*step)}(0) = f^{step}(0), next to find the least i such that f^{(i+step)}(0) = f^{i}(0); we already know such i exists, and must be positive because values of elements in the array cannot be zero
        slow = 0
        while slow != fast:
            slow = iterateNext(slow, nums, N)
            fast = iterateNext(fast, nums, N)

        return fast

class TestFundDuplicateNumber(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_nums': [1,1],
        'test_output': 1,
    }, {
        'test_nums': [1,2,1],
        'test_output': 1,
    }, {
        'test_nums': [2,1,2],
        'test_output': 2,
    }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            answer = obj.findDuplicate(test_case['test_nums'])
            expected = test_case['test_output']

            self.assertEqual(answer, expected)

if __name__ == '__main__':
    main()

