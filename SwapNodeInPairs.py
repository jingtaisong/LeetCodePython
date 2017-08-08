from unittest import (TestCase, main)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createListNodeFromList(list):
    if not len(list):
        return None

    curr = ListNode(0)  # dummy
    preHead = curr

    for item in list:
        curr.next = ListNode(item)
        curr = curr.next

    return preHead.next

def createListFromListNode(head):
    """
    :type head: ListNode 
    :rtype: list
    """
    list = []
    curr = head
    while curr != None:
        list.append(curr.val)
        curr = curr.next

    return list


class SwapNodesInPairs(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        prev = head
        curr = head.next
        grandPrev = ListNode(0)  # Dummy node
        newHead = curr  # to be returned

        while curr != None:
            grandPrev.next = curr
            prev.next = curr.next
            curr.next = prev

            # update
            grandPrev = prev
            prev = grandPrev.next
            if prev != None:
                curr = prev.next
            else:
                curr = None

        return newHead


class TestSwapNodesInPairs(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_input_list': [],
            'test_output_list': []
        }, {
            'test_input_list': [1,2,3,4],
            'test_output_list': [2,1,4,3]
        }]

    def test_result(self):
        obj = SwapNodesInPairs()

        for test_case in self.test_object:
            head_input = createListNodeFromList(test_case['test_input_list'])
            head_output = obj.swapPairs(head_input)
            list_output = createListFromListNode(head_output)

            self.assertEqual(list_output, test_case['test_output_list'])

if __name__ == '__main__':
    main()
