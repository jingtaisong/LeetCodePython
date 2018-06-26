from unittest import (TestCase, main)


def threeWayPartition(array, low, high):
    # array is muted
    n = len(array)
    start = 0
    end = n - 1
    for i in range(0, n):
        if i > end:
            break  # no need to proceed

        if array[i] < low:
            array[start], array[i] = array[i], array[start]
            start += 1
        elif array[i] > high:
            array[end], array[i] = array[i], array[end]
            end -= 1

    return (start, end)  # elements in range(0, start) are < low, elements in range(end+1, n) are > high


def quickSelect(array, k):
    # array is muted
    if k <= 0:
        raise ValueError('k must be positive!')

    n = len(array)
    if n < k:
        raise ValueError('fewer elements in array than k!')

    pivot = array[0]

    start, end = threeWayPartition(array, pivot, pivot)
    if start >= k:
        return quickSelect(array[0:start], k)
    else:
        return quickSelect(array[start:], k - start)


def findMedian(array):
    n = len(array)
    if n == 0:
        raise ValueError('array is empty, cannot find median')

    if n == 1:
        return array[0]

    if n % 2 == 0:
        lowMedian = quickSelect(array, n / 2 - 1)
        highMedian = quickSelect(array, n / 2)
        median = (lowMedian + highMedian) / 2
    else:
        median = quickSelect(array, (n - 1) / 2)

    return median


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # first find the median.
        # since there exists a valid solution, there can be at most [n/2] elements equal to median
        # do a 3-way selection to partition the array into SMALL (elements smaller than median), MEDIAN (elements equal to median), and BIG (elements bigger than median)
        # MEDIAN[0] - BIG[0] - MEDIAN[1] - BIG[1] - ... - MEDIAN[A] - BIG[A], where A = min(# MEDIAN, # BIG)
        # follow by
        # SMALL[0] - MEDIAN[0] - SMALL[1] - MEDIAN[1] - ... - SMALL[B] - MEDIAN[B], where B = min(# MEDIAN, # SMALL)
        # since # MEDIAN <= n/2, # MEDIAN < # BIG + # SMALL, so A + B >= min (# MEDIAN, # BIG + # SMALL) = # MEDIAN
        # so we have exhausted MEDIAN, and the remaining SMALL AND BIG differ by at most 1
        # if nothing left, done
        # if SMALL and BIG are left equally, follow by one SMALL and one BIG
        # if #SMALL = #BIG + 1, follow by one SMALL and one BIG ending with SMALL
        # if #BIG = #SMALL + 1, AND there exists at least one SMALL, then replace the last SMALL[B] - MEDIAN[B] with SMALL[B] - BIG - MEDIAN[B] and reduce to the case when #BIG = #SMALL
        # otherwise, #SMALL = 0, #BIG = 1, So #MEDIAN = 1 or 0, neither is possible
        self.findMedianAnother(nums, 0, len(nums) - 1)
        half = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def findMedianAnother(self, nums, left, right):
        i = j = k = (left + 1)
        mid = len(nums) // 2
        sentinel = nums[left]
        while k <= right:
            if nums[k] < sentinel:
                nums[k], nums[j] = nums[j], nums[k]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                k += 1
            elif nums[k] > sentinel:
                k += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
                k += 1
        nums[left], nums[i - 1] = nums[i - 1], nums[left]
        if i - 1 <= mid < j:
            return nums[mid]
        if mid >= j:
            return self.findMedianAnother(nums, j, right)
        else:
            return self.findMedianAnother(nums, left, i - 2)


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [1,5,1,1,6,4],
            'answer': [1,6,1,5,1,4]
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            obj.wiggleSort(test_case['test_nums'])
            self.assertEqual(test_case['test_nums'], test_case['answer'])
if __name__ == '__main__':
    main()
