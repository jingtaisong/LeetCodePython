# O(nk) time complexity but with a PRECISE answer; the leetcode wants an algorithm with O(n(log(max - min))) time complexity, but at the sacrifice of preciseness

from unittest import (TestCase, main)


class maxAverageII(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # dynamic programming; store an array of k-arrays, each k-array's i-th element is a number standing for the average of the subsequent (i+1) elements before this element (inclusive) when i<=k-2, while the (k-1)-th element is a tuple standing for the maximal average of the subsequent at least k elements before this element (inclusive), and update dynamically
        dynamicAverageTracking = []
        maxAverageFromK = -float('inf')
        for index, element in enumerate(nums):
            if index == 0:
                if k == 1:
                    thisAverages = [(1, element)]
                    maxAverageFromK = max(maxAverageFromK, element)
                else:
                    thisAverages = [element]
                    for j in range(0, k-2):
                        thisAverages.append(-float('inf'))
                    thisAverages.append((1, -float('inf')))
                dynamicAverageTracking.append(
                    thisAverages)  # initialize by element, (k-2) copies of -infty and a tuple (1,-infty)
            else:
                prevAverages = dynamicAverageTracking[-1]
                thisAverages = []  # to be calculated one by one
                for k_index in range(0, k):
                    if k_index == 0:
                        if k == 1:
                            prevKNum, prevKAverage = prevAverages[0]
                            newAverageFromK = float(prevKAverage * prevKNum + element) / (prevKNum + 1)
                            newAverageFromBelowK = element
                            if newAverageFromK >= newAverageFromBelowK:
                                newAverage = newAverageFromK
                                newAverageNum = prevKNum + 1
                            else:
                                newAverage = newAverageFromBelowK
                                newAverageNum = 1
                            thisAverages.append((newAverageNum, newAverage))
                            maxAverageFromK = max(maxAverageFromK, newAverage)
                        else:
                            thisAverages.append(element)
                    elif k_index <= k - 2:
                        newAverage = float(prevAverages[k_index - 1] * k_index + element) / (k_index + 1)
                        thisAverages.append(newAverage)
                    else:  # the maximal average k is the larger between the average by appending element to the previous maximal average k and appending element to the previous average k-1
                        prevKNum, prevKAverage = prevAverages[k - 1]
                        newAverageFromK = float(prevKAverage * prevKNum + element) / (prevKNum + 1)
                        # we know k > 1 at this point
                        newAverageFromBelowK = float(prevAverages[k - 2] * (k - 1) + element) / k
                        if newAverageFromBelowK >= newAverageFromK:
                            newAverage = newAverageFromBelowK
                            newAverageNum = k
                        else:
                            newAverage = newAverageFromK
                            newAverageNum = prevKNum + 1
                        thisAverages.append((newAverageNum, newAverage))
                        maxAverageFromK = max(maxAverageFromK, newAverage)
                dynamicAverageTracking.append(thisAverages)
        return maxAverageFromK


class TestMaxAverageII(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [1,12,-5,-6,50,3],
            'test_k': 4,
            'test_output': 12.75
        }, {
            'test_nums': [1, 2, 3, 4],
            'test_k': 1,
            'test_output': 4
        }, {
            'test_nums': [5],
            'test_k': 1,
            'test_output': 5
        }]

    def test_result(self):
        obj = maxAverageII()

        for test_case in self.test_object:
            result = obj.findMaxAverage(test_case['test_nums'], test_case['test_k'])

            self.assertEqual(test_case['test_output'], result)

if __name__ == '__main__':
    main()
