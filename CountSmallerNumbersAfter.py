from unittest import (TestCase, main)

class CountSmallerToTheRight(object):
    def mergeSortWithInverseOrderCount(self, nums, low, high, counts):
        """
        mergeSort an array nums on [low, high), adjust counts[i] by the number of elements from the right of nums[i] to the left of nums[i]
        """
        if low >= high:
            raise ValueError(
                'low index {lowIndex} cannot be higher than or equal to the high index {highIndex}'.format(lowIndex=low,
                                                                                                           highIndex=high))
        elif low == high - 1:
            return [nums[low]]  # no need to do anything if low == high - 1
        else:
            mid = (low + high) // 2  # guaranteed that low < mid < high
            sortedLowToMid = self.mergeSortWithInverseOrderCount(nums, low, mid, counts)
            sortedMidToHigh = self.mergeSortWithInverseOrderCount(nums, mid, high, counts)
            # mergeSort:
            sortedLowToHigh = []
            lowInd = low
            highInd = mid

            while lowInd < mid and highInd < high:
                if sortedLowToMid[lowInd - low]['value'] > sortedMidToHigh[highInd - mid]['value']:
                    sortedLowToHigh.append(sortedMidToHigh[highInd - mid])
                    highInd += 1
                else:
                    sortedLowToHigh.append(sortedLowToMid[lowInd - low])
                    # when we decide to add an element in LowToMid,
                    # we count how many elements have been added from MidToHigh,
                    # and that is the number of elements that have been moved to the left of this element in LowToMid
                    counts[sortedLowToMid[lowInd - low]['index']] += highInd - mid
                    lowInd += 1

            if highInd < high:
                while highInd < high:  # trailing elements in MidToHigh
                    sortedLowToHigh.append(sortedMidToHigh[highInd - mid])
                    highInd += 1
            elif lowInd < mid:
                while lowInd < mid:    # trailing elements in LowToMid
                    sortedLowToHigh.append(sortedLowToMid[lowInd - low])
                    counts[sortedLowToMid[lowInd - low]['index']] += highInd - mid  # also do this for the trailing elements in LowToMid
                    lowInd += 1

            ind = len(sortedLowToHigh)
            if ind != high - low:
                raise ValueError(
                    'ind {indVal} must be equal to high {highVal} minus low {lowVal}'.format(indVal=ind, highVal=high,
                                                                                             lowVal=low))

            return sortedLowToHigh

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not len(nums):
            return []
        else:
            augmentedNums = []
            augmentedNumsIndex = 0
            for x in nums:
                # index will keep track the original position of an element
                # this is important because we need to keep track the number of elements moved to the left of each original position
                # during the mergeSort procedure
                augmentedNums.append({'index': augmentedNumsIndex, 'value': x})
                augmentedNumsIndex += 1

            counts = [0] * len(nums)
            self.mergeSortWithInverseOrderCount(augmentedNums, 0, len(nums), counts)
            return counts


class TestCountSmallerToTheRight(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [21, 84,66,65,36,100,41],
            'test_output': [0, 4,3,2,0,1,0],
        }]

    def test_result(self):
        obj = CountSmallerToTheRight()

        for test_case in self.test_object:
            result = obj.countSmaller(test_case['test_nums'])

            self.assertEqual(test_case['test_output'], result)

if __name__ == '__main__':
    main()
