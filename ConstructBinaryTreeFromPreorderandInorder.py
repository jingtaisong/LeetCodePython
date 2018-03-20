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
    def buildTreeInternal(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode or None
        """
        if not len(preorder) or not len(inorder):
            if len(preorder) or len(inorder):
                raise ValueError('in order is not empty while preorder is empty!')
            else:
                return None

        # now we know preorder and inorder are nonempty
        root = preorder[0]
        rootIndex = inorder.index(root)

        leftInorder = [x for x in inorder[:rootIndex]]
        rightInorder = [x for x in inorder[rootIndex + 1:]]

        # take the shorter one to test side in preorder list to save time
        if rootIndex < len(preorder) / 2:
            InorderSet = set(leftInorder)
            InorderSetIsLeft = True
        else:
            InorderSet = set(rightInorder)
            InorderSetIsLeft = False

        leftPreorder = []
        rightPreorder = []

        for item in preorder:
            if item != root:
                if item in InorderSet:
                    if InorderSetIsLeft:
                        leftPreorder.append(item)
                    else:
                        rightPreorder.append(item)
                else:
                    if InorderSetIsLeft:
                        rightPreorder.append(item)
                    else:
                        leftPreorder.append(item)

        rootNode = TreeNode(root)
        rootNode.left = self.buildTreeInternal(leftPreorder, leftInorder)
        rootNode.right = self.buildTreeInternal(rightPreorder, rightInorder)
        return rootNode

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeInternal(preorder, inorder)

class TestConstructBinaryTreeFromPreorderInorder(TestCase):
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
            'test_preorder': [1],
            'test_inorder': [1],
            'test_tree': [1],
        }, {
            'test_preorder': [1,2],
            'test_inorder': [2,1],
            'test_tree': [1,2,None],
        }, {
            'test_preorder': [1,2],
            'test_inorder': [1,2],
            'test_tree': [1,None,2],
        }, {
            'test_preorder': [1,2,3],
            'test_inorder': [2,1,3],
            'test_tree': [1,2,3],
        }, {
            'test_preorder': [1,2,3,4],
            'test_inorder': [4,2,1,3],
            'test_tree': [1,2,3,4,None,None,None],
        }, {
            'test_preorder': [1,2,3,4],
            'test_inorder': [2,4,1,3],
            'test_tree': [1,2,3,None,4,None,None],
        }, {
            'test_preorder': [1,2,3,4],
            'test_inorder': [2,1,4,3],
            'test_tree': [1,2,3,None,None,4,None],
        }, {
            'test_preorder': [1,2,3,4],
            'test_inorder': [2,1,3,4],
            'test_tree': [1,2,3,None,None,None,4],
        }, {
            'test_preorder': [3,9,20,15,7],
            'test_inorder': [9,3,15,20,7],
            'test_tree': [3,9,20,None,None,15,7],
        }]

    def test_result(self):
        obj = Solution()
        for test_case in self.test_object:
            test_tree = obj.buildTree(test_case['test_preorder'], test_case['test_inorder'])
            test_tree_array = self.printArrayFromTree(test_tree)
            self.assertEqual(test_tree_array, test_case['test_tree'])

if __name__ == '__main__':
    main()
