from unittest import (TestCase, main)


class maxAverageI(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        1<=k<=n
        """
        n = len(nums)

        if n == 0:
            raise ValueError('cannot have empty array!')
        elif k <= 0:
            raise ValueError('must have a positive {num_k}'.format(num_k=k))
        elif n < k:
            raise ValueError('the length of the array should be at least {num_k}'.format(num_k=k))

        maxMovingKSum = movingKSum = sum(nums[:k])

        if k == n:
            return float(movingKSum) / k

        front = k
        back = 0

        while front < n:
            movingKSum += nums[front] - nums[back]
            maxMovingKSum = max(maxMovingKSum, movingKSum)
            front += 1
            back += 1

        return float(maxMovingKSum) / k


class TestMaxAverageI(TestCase):
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
            'test_k': 4,
            'test_output': 2.5
        }]

    def test_result(self):
        obj = maxAverageI()

        for test_case in self.test_object:
            result = obj.findMaxAverage(test_case['test_nums'], test_case['test_k'])

            self.assertEqual(test_case['test_output'], result)

if __name__ == '__main__':
    main()
