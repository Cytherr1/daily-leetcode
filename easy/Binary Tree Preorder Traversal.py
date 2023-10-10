# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):

        values = []

        def travel(node):
            if node:
                values.append(node.val)
                travel(node.left)
                travel(node.right)

        travel(root)

        return values