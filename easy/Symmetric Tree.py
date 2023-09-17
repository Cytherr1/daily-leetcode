# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):

        leftTree = []
        rightTree = []

        def inOrder(node):
            if node:
                inOrder(node.left)

                inOrder(node.right)

                leftTree.append(node.val)         
            else:
                leftTree.append(-101)

        def reverseOrder(node):
            if node:
                reverseOrder(node.right)

                reverseOrder(node.left)

                rightTree.append(node.val)     
            else:
                rightTree.append(-101)

        inOrder(root.left)
        reverseOrder(root.right)

        print(leftTree)
        print(rightTree)

        if leftTree == rightTree:
            return True
        
        return False