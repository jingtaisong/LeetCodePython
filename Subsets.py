from unittest import (TestCase, main)

from functools import cmp_to_key

class Subsets(object):
    def subsetsHelper(self, nums, existingSets):
        if len(nums) == 0:
            return existingSets
        else:
            s = nums.pop()
            existingSetsLength = len(existingSets)
            for i in range(0, existingSetsLength):
                copySet = [x for x in existingSets[i]]
                copySet.append(s)
                existingSets.append(copySet)
            return self.subsetsHelper(nums, existingSets)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsHelper(nums, [[]])


class TestGenerateParenthesis(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_nums': [1,2,3],
        'test_output': [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ],
    }]

    def test_result(self):
        obj = Subsets()

        def deepCompare(listA, listB):
            if len(listA) < len(listB):
                return -1
            elif len(listA) > len(listB):
                return 1
            else:
                copyA = [x for x in listA]
                copyB = [x for x in listB]
                sorted(copyA)
                sorted(copyB)
                for i, item in enumerate(copyA):
                    if item < copyB[i]:
                        return -1
                    elif item > copyB[i]:
                        return 1
                return 0

        for test_case in self.test_object:
            answer = obj.subsets(test_case['test_nums'])
            answer = [sorted(x) for x in answer]
            answer = sorted(answer, key=cmp_to_key(deepCompare))
            expected = test_case['test_output']
            expected = [sorted(x) for x in expected]
            expected = sorted(expected, key=cmp_to_key(deepCompare))

            self.assertEqual(answer, expected)

if __name__ == '__main__':
    main()

