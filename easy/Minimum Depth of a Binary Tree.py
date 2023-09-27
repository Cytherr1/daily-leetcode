import heapq as hq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root) -> int:
        minHeap = []
        minDepth = 0

        def travel(node, d=1):
            if node:
                if node.left == None and node.right == None:
                    hq.heappush(minHeap, d)
                
                travel(node.left, d + 1)
                travel(node.right, d + 1)
        
        if root:
            travel(root)
            minDepth = hq.heappop(minHeap)
            return minDepth

        return minDepth
        