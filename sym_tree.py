# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    
    def isMirror(self,root1,root2):
        #base case
        if ((not root1) and (not root2)):
            return True
        #other base case
        elif ((not root1) or (not root2)):
            return False
        
        #see if the mirror is correct
        else:
            
            mirror = ((root1.val == root2.val) and (self.isMirror(root1.left,root2.right)) and (self.isMirror(root1.right,root2.left)))
            return mirror
            
