# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        
        pList = []
        qList = []

        def preOrder(node, anyList):
            if node:
                anyList.append(node.val)

                preOrder(node.left, anyList)

                preOrder(node.right, anyList)
            else:
                anyList.append(0)
        
        preOrder(p, pList)
        preOrder(q, qList)

        if pList == qList:
            return True
        
        return False