from unittest import (TestCase, main)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class Solution(object):
    def visitNode(self, root, count):
        if root is None:
            raise ValueError('should not visit a null node!')
        elif count < 0:
            raise ValueError('count should never drop below zero!')
        elif count == 0:
            return 0, True, root.val
        else:
            return count - 1, False, None

    def preOrderTraverse(self, root, count, found, ans):
        if found or root is None:  # don't do anything if already found or if the root node is Null
            return count, found, ans

        count, found, ans = self.preOrderTraverse(root.left, count, found, ans)
        if found:
            return count, found, ans

        count, found, ans = self.visitNode(root, count)
        if found:
            return count, found, ans

        count, found, ans = self.preOrderTraverse(root.right, count, found, ans)
        if found:
            return count, found, ans

        return count, found, ans

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count, found, ans = self.preOrderTraverse(root, k - 1, False, None)
        return ans


class TestMostFrequentK(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_tree': "[3,1,4,null,2]",
            'test_k': 1,
            'answer': 1
        }, {
            'test_tree': "[5,3,6,2,4,null,null,1]",
            'test_k': 3,
            'answer': 3
        }]

    def test_result(self):
        obj = Solution()
        for i, test_case in enumerate(self.test_object):
            root = stringToTreeNode(test_case['test_tree'])
            answer = obj.kthSmallest(root, test_case['test_k'])
            self.assertEqual(answer, test_case['answer'])

if __name__ == '__main__':
    main()
