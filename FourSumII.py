from unittest import (TestCase, main)
from collections import Counter

def countSumMatch(table1, table2, target):
    """
    table = [{ element : e_{i, *}, weight : w_{i, *} }]
    table1 and table2 have the same length and assume the elements are sorted
    count sum w_{i, 1}w_{i, 2} over e_{i, 1} + e_{i, 2} = target
    """
    l1 = len(table1)
    l2 = len(table2)

    i = l1 - 1
    j = 0
    count = 0

    while i >= 0 or j < l2:
        currentSum = table1[i]['element'] + table2[j]['element']

        if currentSum == target:
            count += table1[i]['weight'] * table2[j]['weight']

        if currentSum <= target:
            if j + 1 < l2:
                j += 1
            else:
                break
        else:
            if i - 1 >= 0:
                i -= 1
            else:
                break

    return count

class fourListsSumCount(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        AB = []
        for i in A:
            for j in B:
                AB.append(i + j)

        counterAB = Counter(AB).most_common()
        Table1 = [{'element': x, 'weight': y} for x, y in counterAB]

        CD = []
        for i in C:
            for j in D:
                CD.append(i + j)

        counterCD = Counter(CD).most_common()
        Table2 = [{'element': x, 'weight': y} for x, y in counterCD]

        return countSumMatch(Table1, Table2, 0)

class TestFourListsSumCount(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_input_lists': [[1,2], [-2, -1], [-1, 2], [0,2]],
            'test_output': 2
        }]

    def test_result(self):
        obj = fourListsSumCount()

        for test_case in self.test_object:
            output = obj.fourSumCount(test_case['test_input_lists'][0], test_case['test_input_lists'][1], test_case['test_input_lists'][2], test_case['test_input_lists'][3])

            self.assertEqual(output, test_case['test_output'])

if __name__ == '__main__':
    main()
