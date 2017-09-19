from unittest import (TestCase, main)

class SortColorsLinearTimeConstantSpace(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        linear time complexity, constant space complexity
        """
        counts0 = 0
        counts1 = 0
        counts2 = 0

        for item in nums:
            if item == 0:
                nums[counts0] = 0
                if counts1 > 0:
                    nums[counts0 + counts1] = 1
                if counts2 > 0:
                    nums[counts0 + counts1 + counts2] = 2
                counts0 += 1
            elif item == 1:
                nums[counts0 + counts1] = 1
                if counts2 > 0:
                    nums[counts0 + counts1 + counts2] = 2
                counts1 += 1
            elif item == 2:
                counts2 += 1
            else:
                raise ValueError('item can only be among 0, 1, and 2! but now found {x}'.format(x=item))

class TestSortColors(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [1],
            'test_output': [1],
        }, {
            'test_nums': [1,0],
            'test_output': [0,1],
        }, {
            'test_nums': [1,2],
            'test_output': [1,2],
        }, {
            'test_nums': [1,1,2,0],
            'test_output': [0,1,1,2],
        }]

    def test_result(self):
        obj = SortColorsLinearTimeConstantSpace()

        for test_case in self.test_object:
            nums = test_case['test_nums']
            result = obj.sortColors(nums)

            self.assertEqual(nums, test_case['test_output'])

if __name__ == '__main__':
    main()