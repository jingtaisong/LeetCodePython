from unittest import (TestCase, main)


class Solution(object):
    def findPeakElementInternal(self, nums, start, end):
        # find the index of a peak element in the subarray nums[start: end]; start <= end
        if start == end:
            return -1

        if start == end - 1:
            return start

        mid = int((start + end) / 2)
        # now guaranteed 0 <= start < mid < end
        firstHalfPeakIndex = self.findPeakElementInternal(nums, start, mid)
        secondHalfPeakIndex = self.findPeakElementInternal(nums, mid, end)

        # guaranteed firstHalfPeakIndex != -1 and secondHalfPeakIndex != -1
        if firstHalfPeakIndex == -1:
            raise ValueError(
                'should not expect first half not having a peak! start = {s}, mid = {m}'.format(s=start, m=mid))

        if secondHalfPeakIndex == -1:
            raise ValueError(
                'should not expect second half not having a peak! mid = {m}, end = {e}'.format(m=mid, e=end))

        if firstHalfPeakIndex != mid - 1:
            return firstHalfPeakIndex

        if secondHalfPeakIndex != mid:
            return secondHalfPeakIndex

        # now nums[mid - 1] > nums[mid - 2] and nums[mid] > nums[mid + 1]
        if nums[mid - 1] < nums[mid]:
            return mid

        if nums[mid - 1] > nums[mid]:
            return mid - 1

        raise ValueError('should not expect two neighbours to be equal! index {a} and {b}'.format(a=mid - 1, b=mid))

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.findPeakElementInternal(nums, 0, n)

class TestPeakElement(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [],
        }, {
            'test_nums': [1,2,3,1],
        }, {
            'test_nums': [1,2],
        }, {
            'test_nums': [2,1],
        }, {
            'test_nums': [1,2,1,3,5,6,4],
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            testNums = test_case['test_nums']
            ans = obj.findPeakElement(testNums)
            n = len(testNums)
            if ans == -1:
                self.assertEqual(n, 0)
            elif ans == 0:
                self.assertGreater(testNums[ans], testNums[ans+1])
            elif ans == n-1:
                self.assertLess(testNums[ans-1], testNums[ans])
            else:
                self.assertLess(testNums[ans-1], testNums[ans])
                self.assertGreater(testNums[ans], testNums[ans+1])

if __name__ == '__main__':
    main()
