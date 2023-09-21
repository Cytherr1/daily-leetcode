# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        depths = []

        if root:
            def preOrder(node, depth=0):
                if node:
                    depths.append(depth + 1)
                    preOrder(node.left, depth + 1)
                    preOrder(node.right, depth + 1)

            preOrder(root, 0)
        
            return max(depths)
        
        return 0