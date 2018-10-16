from unittest import (TestCase, main)

def sqDist(p1, p2):
    return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for p1 in points:
            distCountList = dict()
            for p2 in points:
                sqDistPt = sqDist(p1, p2)
                sqDistPtInStr = str(sqDistPt)
                distCountList[sqDistPtInStr] = distCountList.get(sqDistPtInStr, 0) + 1
            for ct in distCountList.values():
                count += ct * (ct - 1)

        return count

class TestNumberOfBoomerangs(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_points': [],
            'ans': 0
        }, {
            'test_points': [[0,0]],
            'ans': 0
        }, {
            'test_points': [[0,0], [0,1]],
            'ans': 0
        }, {
            'test_points': [[0,0], [0,1], [0,2]],
            'ans': 2
        }, {
            'test_points': [[0,1], [0,0], [0,2]],
            'ans': 2
        }, {
            'test_points': [[0,2], [0,0], [0,1]],
            'ans': 2
        }]

    def test_result(self):
        obj = Solution()

        for test_case in self.test_object:
            ans = obj.numberOfBoomerangs(test_case['test_points'])
            self.assertEqual(ans, test_case['ans'])

if __name__ == '__main__':
    main()
