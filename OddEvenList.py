from unittest import (TestCase, main)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        oddHead = head
        evenHead = head.next

        oddMarker = head
        evenMarker = head.next

        while evenMarker.next != None:
            oddMarker.next = evenMarker.next
            oddMarker = evenMarker.next
            if oddMarker.next == None:
                evenMarker.next = None
                oddMarker.next = evenHead
                return oddHead
            else:
                evenMarker.next = oddMarker.next
                evenMarker = evenMarker.next

        oddMarker.next = evenHead
        return oddHead

def linkedListToArray(head):
    array = []
    mark = head
    while mark != None:
        array.append(mark.val)
        mark = mark.next
    return array

def arrayToLinkedList(array):
    n = len(array)
    if not n:
        return None
    head = ListNode(array[0])
    mark = head
    for i in range(1, n):
        mark.next = ListNode(array[i])
        mark = mark.next
    return head

class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_linkedList': [1,2],
            'answer': [1,2]
        }, {
            'test_linkedList': [1, 2, 3],
            'answer': [1, 3, 2]
        }, {
            'test_linkedList': [1, 2, 3, 4],
            'answer': [1, 3, 2, 4]
        }, ]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            testLinkedList = arrayToLinkedList(test_case['test_linkedList'])
            answerLinkedList = obj.oddEvenList(testLinkedList)
            answerPrinted = linkedListToArray(answerLinkedList)
            self.assertEqual(answerPrinted, test_case['answer'])

if __name__ == '__main__':
    main()
