# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        
        values = []

        def travel(node, currentSum):
            if node:
                currentSum += node.val
                if node.left == None and node.right == None:
                    values.append(currentSum)
                
                travel(node.left, currentSum)
                travel(node.right, currentSum)

        travel(root, 0)

        return targetSum in values