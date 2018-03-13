from unittest import (TestCase, main)

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def TreesEqual(p, q):
    if p == None and q == None:
        return True

    if p == None or q == None:
        return False

    # now p and q are both not None
    if p.val != q.val:
        return False

    leftEqual = TreesEqual(p.left, q.left)
    if not leftEqual:
        return False

    rightEqual = TreesEqual(p.right, p.right)
    if not rightEqual:
        return False

    return True

class Solution(object):
    def visit(self, node, p, q):
        self.visitedP = self.visitedP or TreesEqual(node, p)
        self.visitedQ = self.visitedQ or TreesEqual(node, q)

        if (not self.visitedP and self.visitedQ) or (self.visitedP and not self.visitedQ):
            if (self.lowestLevelUntilBothVisited == None) or (self.lowestLevelUntilBothVisited > self.currentLevel):
                self.lowestLevelUntilBothVisited = self.currentLevel

        # LCA is the first level that is lower than any level we met in between visiting P and visiting Q
        if self.visitedP and self.visitedQ:
            if (self.lowestLevelUntilBothVisited != None) and (self.currentLevel < self.lowestLevelUntilBothVisited):
                return node

        return None

    def postOrderTraverse(self, node, p, q):
        currentLevel = self.currentLevel
        answer = None

        if node.left != None:
            self.currentLevel = currentLevel + 1
            answer = self.postOrderTraverse(node.left, p, q)
            if answer != None:
                return answer

        if node.right != None:
            self.currentLevel = currentLevel + 1
            answer = self.postOrderTraverse(node.right, p, q)
            if answer != None:
                return answer

        self.currentLevel = currentLevel
        answer = self.visit(node, p, q)
        return answer

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # initialize booleans visitedP, visitedQ, lowestLevelUntilBothVisited, currentLevel
        self.visitedP = False
        self.visitedQ = False
        self.lowestLevelUntilBothVisited = None
        self.currentLevel = 0
        self.answer = None

        if p == q:
            return p

        answer = self.postOrderTraverse(root, p, q)
        return answer


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

    def printArrayFromTree(self, root):
        if root == None:
            return []

        nodeList = deque([(root, 0)])
        maxLevel = 0
        nextPartArray = []
        output = []

        while len(nodeList) or len(nextPartArray):
            node, level = nodeList.popleft()

            # print out this node
            if node == None:
                output.append(None)
            else:
                output.append(node.val)

            if level > maxLevel:
                maxLevel = level

            # amend nextPartArray
            if node == None:
                nextPartArray.append((None, level+1))
                nextPartArray.append((None, level+1))
            else:
                if node.left == None:
                    nextPartArray.append((None, level+1))
                else:
                    nextPartArray.append((node.left, level+1))

                if node.right == None:
                    nextPartArray.append((None, level+1))
                else:
                    nextPartArray.append((node.right, level+1))

            # if nextPartArray is full, determine whether to stop or concat nodeList with nextPartArray
            if len(nextPartArray) == pow(2, maxLevel+1):
                allNone = True
                for nextNode, nextLevel in nextPartArray:
                    if nextNode != None:
                        allNone = False
                        break
                if allNone:
                    return output
                else:
                    nodeList = deque()
                    for nextNode, nextLevel in nextPartArray:
                        nodeList.append((nextNode, nextLevel))
                    nextPartArray = []


    def setUp(self):
        self.test_object = [{
        'test_tree': [37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22],
        'test_p': [-100,-54,None],
        'test_q': [48,-71,-22],
        'test_output': [-48,-100,48,-54,None,-71,-22]
    },{
        'test_tree': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None],
        'test_p': [7],
        'test_q': [4],
        'test_output': [2,7,4]
    }, {
        'test_tree': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None],
        'test_p': [6],
        'test_q': [0],
        'test_output': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None]
    }, {
        'test_tree': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None],
        'test_p': [6],
        'test_q': [8],
        'test_output': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None]
    }, {
        'test_tree': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None],
        'test_p': [5,6,2,None,None,7,4],
        'test_q': [8],
        'test_output': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None]
    }, {
        'test_tree': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None],
        'test_p': [5,6,2,None,None,7,4],
        'test_q': [1,0,8],
        'test_output': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None]
    }, {
        'test_tree': [3,5,1,6,2,0,8,None,None,7,4,None,None,None,None],
        'test_p': [5,6,2,None,None,7,4],
        'test_q': [4],
        'test_output': [5,6,2,None,None,7,4]
    }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            test_tree = self.buildTreeFromArray(test_case['test_tree'])
            test_p = self.buildTreeFromArray(test_case['test_p'])
            test_q = self.buildTreeFromArray(test_case['test_q'])
            answerTree = obj.lowestCommonAncestor(test_tree, test_p, test_q)
            answer = self.printArrayFromTree(answerTree)

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()
