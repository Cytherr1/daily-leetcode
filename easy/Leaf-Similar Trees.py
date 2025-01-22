# Definition for a binary tree node.
class TreeNode:
		def __init__(self, val=0, left=None, right=None):
				self.val = val
				self.left = left
				self.right = right
class Solution:
		def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
						
			def inOrder(node):
					if node:
							yield from inOrder(node.left)

							if node.left == None and node.right == None:
								yield node.val

							yield from inOrder(node.right)
            
			return [i for i in inOrder(root1)] == [i for i in inOrder(root2)]