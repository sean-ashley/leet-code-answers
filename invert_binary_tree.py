# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def invertTree(self, root: TreeNode) -> TreeNode: 
        
        dummy = root
        
        #base cases
        if not root:
            return 
        
        #swap roots
        root.left,root.right = root.right,root.left
        
        #recursive call down the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return dummy
