from unittest import (TestCase, main)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodeList = deque()
        prevLevel = -1
        output = []

        if root == None:
            return output
        nodeList.append((0, root))

        while len(nodeList):
            currLevel, currNode = nodeList.popleft()
            if currLevel > prevLevel:
                currLevelOutput = []
            else:
                currLevelOutput = output[-1]
            currLevelOutput.append(currNode.val)
            if currLevel > prevLevel:
                output.append(currLevelOutput)
            prevLevel = currLevel

            if currNode.left != None:
                nodeList.append((currLevel + 1, currNode.left))
            if currNode.right != None:
                nodeList.append((currLevel + 1, currNode.right))
        return output


class TestBinaryTreeLevelOrder(TestCase):
    """
    Regtest
    """
    def buildTreeFromArray(self, array):
        if not len(array) or array[0] is None:
            return None

        root = TreeNode(array[0])

        leftArray = []
        rightArray = []

        index = 1
        level = 1
        while index < len(array):
            halfSizeLevel = pow(2, level - 1)
            for i in range(0, halfSizeLevel):
                leftArray.append(array[index + i])
            for i in range(halfSizeLevel, 2*halfSizeLevel):
                rightArray.append(array[index + i])
            index += 2 * halfSizeLevel
            level += 1

        leftTree = self.buildTreeFromArray(leftArray)
        rightTree = self.buildTreeFromArray(rightArray)

        root.left = leftTree
        root.right = rightTree

        return root

    def setUp(self):
        self.test_object = [{
        'test_tree': [3,9,20,None,None,15,7],
        'test_output': [
          [3],
          [9,20],
          [15,7]
        ]
    }, {
        'test_tree': [3,None,20],
        'test_output': [
          [3],
          [20],
        ]
    }, {
        'test_tree': [3,None,20,None,None,9,None],
        'test_output': [
          [3],
          [20],
          [9]
        ]
    }, {
        'test_tree': [3,4,5,6,7,8,9],
        'test_output': [
          [3],
          [4,5],
          [6,7,8,9]
        ]
    }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            test_tree = self.buildTreeFromArray(test_case['test_tree'])
            answer = obj.levelOrder(test_tree)
            expected = test_case['test_output']

            self.assertEqual(answer, expected)

if __name__ == '__main__':
    main()

