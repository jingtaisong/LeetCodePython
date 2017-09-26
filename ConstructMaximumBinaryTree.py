from unittest import (TestCase, main)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# helper for unittest
def treeNodeToString(root):
    output = ""
    queue = [root]
    length = 1
    current = 0
    while current != length:
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
        length += 2

    return "[" + output[:-2] + "]"

class ConstructMaximumBinaryTree(object):
    def constructFromDecaySequenceAndNums(self, decaySequence, nums):
        """
        :type decaySequence: List[TreeNode]
        :type nums: List[int]
        :rtype: TreeNode
        decaySequence is a list of trees satisfying:
            the roots' values are decreasing
            each tree has no right child
        """
        D = len(decaySequence)
        N = len(nums)

        # ready to construct the tree if the nums list has reached emptyness
        if N == 0:
            dummyRoot = TreeNode(0)
            cursor = dummyRoot
            for tree in decaySequence:
                cursor.right = tree
                cursor = cursor.right
            return dummyRoot.right

        # otherwise, if the first element of nums is less than the last root's val in decaySequencce, we put this element as its own trivial tree into the decaySequence; if the first element of nums is greater than the last root's val in decaySequence, we trace back until we find a root's val beats this element, put the middle decaySequencce on the left child of this element, and put it into the decaySequence
        leadingElement = nums[0]
        if D == 0 or decaySequence[D - 1].val > leadingElement:
            newDecayElement = TreeNode(leadingElement)
            decaySequence.append(newDecayElement)
        else:
            tracebackCursor = D - 1
            while tracebackCursor > 0 and decaySequence[tracebackCursor - 1].val < leadingElement:
                tracebackCursor -= 1

            leftChild = decaySequence[tracebackCursor]
            leftChildCursor = leftChild
            for i in range(tracebackCursor+1, D):
                leftChildCursor.right = decaySequence[i]
                leftChildCursor = leftChildCursor.right

            newDecayElement = TreeNode(leadingElement)
            newDecayElement.left = leftChild
            decaySequence = decaySequence[0:tracebackCursor]
            decaySequence.append(newDecayElement)

        result = self.constructFromDecaySequenceAndNums(decaySequence, nums[1:])
        return result

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.constructFromDecaySequenceAndNums([], nums)

class TestConstructMaximumBinaryTree(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [
        {
            'test_nums': [3,2,1,6,0,5],
            'test_output': '[6, 3, 5, null, 2, 0, null, null, 1, null, null, null, null]',
        }]

    def test_result(self):
        obj = ConstructMaximumBinaryTree()

        for test_case in self.test_object:
            nums = test_case['test_nums']
            result = obj.constructMaximumBinaryTree(nums)
            printResult = treeNodeToString(result)

            self.assertEqual(printResult, test_case['test_output'])

if __name__ == '__main__':
    main()