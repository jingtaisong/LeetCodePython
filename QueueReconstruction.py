from unittest import (TestCase, main)


class Solution(object):
    def reconstructQueuePeopleSorted(self, sortedPeople):
        if not len(sortedPeople):
            return []

        shortestPeople = sortedPeople.pop()
        reconstructedQueue = self.reconstructQueuePeopleSorted(sortedPeople)
        reconstructedQueue.insert(shortestPeople[1], shortestPeople)
        return reconstructedQueue

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(people)
        sortedList = sorted(people, reverse=True, key=lambda x: x[0]*N - x[1])
        return self.reconstructQueuePeopleSorted(sortedList)


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_people': [],
            'answer': []
        }, {
            'test_people': [[1,0]],
            'answer': [[1,0]]
        }, {
            'test_people': [[1,0], [1,1]],
            'answer': [[1,0], [1,1]]
        }, {
            'test_people': [[1,0],[2,0]],
            'answer': [[1,0], [2,0]]
        }, {
            'test_people': [[1,1],[2,0]],
            'answer': [[2,0], [1,1]]
        }, {
            'test_people': [[1,1], [1,0]],
            'answer': [[1,0],[1,1]]
        }, {
            'test_people': [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
            'answer': [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            answer = obj.reconstructQueue(test_case['test_people'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
