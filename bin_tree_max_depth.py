# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.best = 0
    def maxDepth(self, root: TreeNode,depth = 1) -> int:
        
        if not root:
            return self.best
        #if we are at a root node
        elif ((not root.left) and (not root.right)):
            self.best = max(self.best,depth)
        
        self.maxDepth(root.left,depth + 1)
        self.maxDepth(root.right,depth + 1)
        return self.best
    
