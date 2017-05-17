from unittest import (TestCase, main)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def binaryLSearch(array, start, end, anchor):
    """
    assuming the array is sorted and all distinct, search the first index in [start, end) at which the element is greater than (strictly) the anchor; if the element at the end index is still less than or equal to the anchor, then return None
    """
    if start >= end:
        raise ValueError("start index {s} cannot be greater than end index {e}".format(s=start, e=end))
    elif start == end - 1:
        if array[start] > anchor:
            return start
        else:
            return None

    # now assume start <= end - 2

    mid = (start + end) // 2  # guaranteed start < mid < end
    if array[mid - 1] >= anchor:
        return binaryLSearch(array, start, mid, anchor)
    else:
        return binaryLSearch(array, mid, end, anchor)


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervalList = []  # intervalList is a table with "start" and "end" columns indicating the start and end of each interval

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        intervalCount = len(self.intervalList)
        if intervalCount == 0:
            self.intervalList.append({'start': val, 'end': val})
            return

        FirstStartGreater = binaryLSearch([item['start'] for item in self.intervalList], 0, intervalCount, val)

        if FirstStartGreater == None:
            if self.intervalList[intervalCount - 1]['end'] < val - 1:
                self.intervalList.append({'start': val, 'end': val})
            else:
                self.intervalList[intervalCount - 1]['end'] = max(self.intervalList[intervalCount - 1]['end'], val)
        elif FirstStartGreater == 0:
            if val < self.intervalList[0]['start'] - 1:
                self.intervalList.insert(0, {'start': val, 'end': val})
            else:
                self.intervalList[0]['start'] = val
        elif val < self.intervalList[FirstStartGreater]['start'] - 1:
            if self.intervalList[FirstStartGreater - 1]['end'] < val - 1:
                self.intervalList.insert(FirstStartGreater, {'start': val, 'end': val})
            else:
                self.intervalList[FirstStartGreater - 1]['end'] = max(self.intervalList[FirstStartGreater - 1]['end'],
                                                                      val)
        else:
            if self.intervalList[FirstStartGreater - 1]['end'] < val - 1:
                self.intervalList[FirstStartGreater]['start'] = val
            else:
                self.intervalList[FirstStartGreater - 1]['end'] = self.intervalList[FirstStartGreater]['end']
                del self.intervalList[FirstStartGreater]

        return

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """

        return [[item['start'], item['end']] for item in self.intervalList]

        # Your SummaryRanges object will be instantiated and called as such:
        # obj = SummaryRanges()
        # obj.addNum(val)
        # param_2 = obj.getIntervals()

class TestDataStreamDisjointIntervals(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_data_stream': [1],
            'test_output': '[1, 1]',
        }, {
            'test_data_stream': [1, 2],
            'test_output': '[1, 2]',
        }, {
            'test_data_stream': [1, 3],
            'test_output': '[1, 1], [3, 3]',
        }, {
            'test_data_stream': [1, 3, 7, 2, 6],
            'test_output': '[1, 3], [6, 7]',
        }]

    def test_result(self):
        for test_case in self.test_object:
            obj = SummaryRanges()

            for data in test_case['test_data_stream']:
                obj.addNum(data)

            self.assertEqual(test_case['test_output'], obj.getIntervals())

if __name__ == '__main__':
    main()