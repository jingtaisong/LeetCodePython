from unittest import (TestCase, main)

class UglyNumber(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Start with L = [1], they exhaust ugly numbers up to 1; Maintain three growing lists by multiplying L by 2, 3, and 5, respectively. Maintain three cursors to record the index when iterating through the three growing lists. Each time find a new ugly number, add it to L as well as the three growing lists. Each time a new number is found, each cursor moves at most by 1, so this is an O(n) algorithm
        uglyList = [1]
        growingList = [{'multiplier': x} for x in [2, 3, 5]]
        for item in growingList:
            item['list'] = [x * (item['multiplier']) for x in uglyList]
            item['cursor'] = 0

        while len(uglyList) < n:
            nextUglyNumber = min([item['list'][item['cursor']] for item in growingList])
            uglyList.append(nextUglyNumber)
            for item in growingList:
                item['list'].append(nextUglyNumber * item['multiplier'])
                cursor = item['cursor']
                while item['list'][cursor] <= nextUglyNumber:
                    cursor += 1
                item['cursor'] = cursor

        return uglyList[n - 1]


class TestUglyNumber(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_n': 1,
            'test_output': 1
        }, {
            'test_n': 10,
            'test_output': 12
        }]

    def test_result(self):
        obj = UglyNumber()

        for test_case in self.test_object:
            result = obj.nthUglyNumber(test_case['test_n'])

            self.assertEqual(test_case['test_output'], result)

if __name__ == '__main__':
    main()
