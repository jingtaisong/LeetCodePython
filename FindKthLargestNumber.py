from unittest import (TestCase, main)


def iParent(x):
    return x // 2


def iLeftChild(x):
    return 2 * x + 1


def iRightChild(x):
    return 2 * x + 2


def repairHeap(array, start, end):
    # assuming all children (before index = end) of start are in good state, repair the heap at index = start
    currentIndex = start

    while True:
        nextIndex = currentIndex  # where to set the next index

        child = iLeftChild(currentIndex)  # consider left child first
        if child > end:  # stop once the left child of the current index is already out of scope, i.e., current index is a leaf
            break
        elif array[child] > array[currentIndex]:
            nextIndex = child  # move the index to left child

        child = iRightChild(currentIndex)  # then consider right child
        if child <= end and array[child] > array[
            nextIndex]:  # if the right child is greater than what we have just decided to swap (could be left child or could be still the root), then move the root to the right child
            nextIndex = child  # move the index to right child

        if nextIndex == currentIndex:
            break  # if we did not move the index at all, we should stop
        else:
            array[currentIndex], array[nextIndex] = array[nextIndex], array[currentIndex] # swap
            currentIndex = nextIndex

    return array


def createHeap(array):
    n = len(array)
    end = n - 1
    start = iParent(end)

    while start >= 0:
        array = repairHeap(array, start,
                           end)  # at the beginning this heap consists of just two nodes, and could spread over time
        start -= 1  # guarantee all nodex are in good state except for the new root node

    return array

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        do HeapSort to iteratively swap the largest element to the back, k times is sufficient for this problem, time complexity O(klog n)
        """
        n = len(nums)
        end = n - 1
        nums = createHeap(nums)

        while end > 0:
            nums[end], nums[0] = nums[0], nums[end]
            # we can guarantee [end, +infty) is sorted and are larger than previous elements, so end is guaranteed to be the (n - end)-th largest element
            if n - end == k:
                return nums[end]

            end -= 1
            nums = repairHeap(nums, 0, end)  # repair the heap on [0, end)

        # if we are here, meaning k = n, so return the current first element
        if k != n:
            raise ValueError(
                'k is expected to be between 0 and {upperbound}, but found {actual}!'.format(upperbound=n, actual=k))
        else:
            return nums[0]


class TestKthLargest(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [
{
    'test_nums': [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6],
    'test_k': 20,
    'test_output': 2
}
        ]

    def test_result(self):
        obj = Solution()

        for test_case in self.test_object:
            answer = obj.findKthLargest(test_case['test_nums'], test_case['test_k'])

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

