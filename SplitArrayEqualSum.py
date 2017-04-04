"""
Given an array and a positive integer n, is it possible to split the array into n segments,
excluding the connection elements between two adjacent elements,
such that each segment has the same sum?
"""
from unittest import (TestCase, main)


def split_array_equal_expected_sum_exist_interval(array, n, expected_sum, start, end):
    """ A helper function: given an array, a positive integer n, an expected sum, a start and end index, is it possible to split the subarray
        of the slice [start, end) in n segments, excluding the connection elements between two adjacent elements, such that the sum of each segment
        is equal to the expected sum?
    :param array: iterable
    :param n: number
    :param expected_sum: number
    :param start: number
    :param end: number
    :return: bool
    """
    if start >= end:
        return False
    elif n == 1 :
        return sum(array[start : end]) == expected_sum
    elif n == 2:
        running_sum = 0
        total_sum = sum(array[start : end]) # save us from another iteration on the second half
        for index in range(start, end):
            item = array[index]
            if running_sum == expected_sum and start < index < end - 1 and 2 * expected_sum + item == total_sum:
                return True

            running_sum += item
        return False
    else:
        running_sum = 0
        for index in range(start, end):
            item = array[index]
            if running_sum == expected_sum and start < index and split_array_equal_expected_sum_exist_interval(array, n-1, expected_sum, index + 1, end):
                return True

            running_sum += item
        return False


def split_array_equal_sum(array, n):
    """ the main function that tells whether it is possible to split an array into n segments,
        excluding the connection elements between two adjacent elements, such that each segment has the same sum
    :param array: iterable
    :param n: number
    :return: bool
    """
    if n == 1:
        return True
    else:
        running_sum = 0
        length = len(array)
        for index in range(0, length):
            item = array[index]
            if index > 0 and split_array_equal_expected_sum_exist_interval(array, n-1, running_sum, index + 1, length):
                return True

            running_sum += item
        return False


class TestSplitArrayEqualSum(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_array': [1,2,1],
            'test_n': 2,
            'test_result': True
        }, {
            'test_array': [1,2,1,2],
            'test_n': 2,
            'test_result': False
        }, {
            'test_array': [1,2,1,2,1,2,1],
            'test_n': 4,
            'test_result': True
        }]

    def test_result(self):
        for test_case in self.test_object:
            self.assertEqual(test_case['test_result'], split_array_equal_sum(test_case['test_array'], test_case['test_n']))


if __name__ == '__main__':
    main()