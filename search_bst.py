# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        # base case
        if root and root.val == val:
            return root
        
        #left tree
        
        elif root and root.val > val:
            return self.searchBST(root.left,val)
        
        #right tree
        elif root and root.val < val:
            return self.searchBST(root.right,val)
