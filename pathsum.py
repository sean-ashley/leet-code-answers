# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int,curr_val = 0) -> bool:
        #edge case
        if not root:
            return False
        
        #if we at leaf node, see if we did it
        elif (not root.left) and (not root.right):
            if curr_val + root.val == targetSum:
                return True
        #recursive case
        return self.hasPathSum(root.left,targetSum,curr_val = curr_val + root.val) or self.hasPathSum(root.right,targetSum,curr_val = curr_val + root.val)
        
        
        
        
        
