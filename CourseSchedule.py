from unittest import (TestCase, main)


class CourseSchedule(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        markedList = [{'isPermanent': False, 'isTemporary': False, 'toNodes': []} for i in
                      range(0, numCourses)]  # list of pairs (isPermanent, isTemporary)

        for [toNode, fromNode] in prerequisites:
            markedList[fromNode]['toNodes'].append(toNode)

        def findFirstUnmarked(mList):
            for index, item in enumerate(mList):
                if not item['isPermanent'] and not item['isTemporary']:
                    return index
            return -1

        def visit(ID):
            if markedList[ID]['isPermanent']: # met a permanently marked node means this node has been searched out, no need to search again
                return False
            if markedList[ID]['isTemporary']: # met a temporarily marked node means we have found a cycle
                return True
            markedList[ID]['isTemporary'] = True
            for toNode in markedList[ID]['toNodes']:
                foundTemporarilyMarked = visit(toNode)
                if foundTemporarilyMarked:
                    return True
            markedList[ID]['isPermanent'] = True
            return False

        while findFirstUnmarked(markedList) != -1:
            IDNum = findFirstUnmarked(markedList)
            foundTemporarilyMarked = visit(IDNum)
            if foundTemporarilyMarked:
                return False

        return True

class TestCourseSchedule(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_n': 2,
        'test_prerequisites': [[1,0]],
        'test_output': True
    }, {
        'test_n': 2,
        'test_prerequisites': [[1,0], [0,1]],
        'test_output': False
    }]

    def test_result(self):
        obj = CourseSchedule()

        for test_case in self.test_object:
            answer = obj.canFinish(test_case['test_n'], test_case['test_prerequisites'])

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

