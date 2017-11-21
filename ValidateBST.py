from unittest import (TestCase, main)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ValidateBST(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        nodeList = list()
        node = root

        lastVisitedValue = None
        Done = False

        while not Done:
            if node is not None:
                nodeList.append(node)
                node = node.left
            else:
                if len(nodeList) == 0:
                    Done = True
                else:
                    node = nodeList.pop()

                    # visit function: compare the node's value against the last visited value and update the last visited value
                    if lastVisitedValue is not None and node.val <= lastVisitedValue:
                        return False
                    else:
                        lastVisitedValue = node.val

                    node = node.right

        return True

class TestValidateBST(TestCase):
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
        'test_tree': [10,5,15,None,None,6,20],
        'test_output': False,
    }, {
        'test_tree': [3,2,None],
        'test_output': True,
    }, {
        'test_tree': [3,None,4],
        'test_output': True,
    }, {
        'test_tree': [2,1,3],
        'test_output': True,
    }, {
        'test_tree': [1,2,3],
        'test_output': False,
    }]

    def test_result(self):
        obj = ValidateBST()

        for test_case in self.test_object:
            test_tree_root = self.buildTreeFromArray(test_case['test_tree'])

            answer = obj.isValidBST(test_tree_root)

            print(test_case['test_tree'])
            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

