# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):

        vals = []

        def travel(node):
            if node:
                travel(node.left)
                travel(node.right)

                vals.append(node.val)

        travel(root)

        return vals