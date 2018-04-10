from unittest import (TestCase, main)


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bitCountList = [0]

        if num == 0:
            return bitCountList

        recentSegmentBitCountList = [1]
        bitCountList.append(1)

        currentLength = 2
        recentSegmentLength = 1

        while currentLength <= num:
            for item in recentSegmentBitCountList:
                bitCountList.append(item)
                currentLength += 1
                if currentLength > num:
                    break

            if currentLength > num:
                break

            for index in range(0, recentSegmentLength):
                recentItem = recentSegmentBitCountList[index]
                recentSegmentBitCountList.append(recentItem + 1)
                bitCountList.append(recentItem + 1)
                currentLength += 1
                if currentLength > num:
                    break

            if currentLength <= num:
                recentSegmentLength *= 2

        return bitCountList


class TestCoinChange(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_num': 1,
            'answer': [0, 1],
        }, {
            'test_num': 2,
            'answer': [0, 1, 1],
        }, {
            'test_num': 3,
            'answer': [0, 1, 1, 2],
        }, {
            'test_num': 4,
            'answer': [0, 1, 1, 2, 1],
        }, {
            'test_num': 5,
            'answer': [0, 1, 1, 2, 1, 2],
        }, {
            'test_num': 6,
            'answer': [0, 1, 1, 2, 1, 2, 2],
        }, {
            'test_num': 7,
            'answer': [0, 1, 1, 2, 1, 2, 2, 3],
        }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            answer = obj.countBits(test_case['test_num'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
