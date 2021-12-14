# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        left_traversal = float("inf")
        right_traversal = float("inf")
        #edge case
        if not root:
            return 0
        #base case, we are at leaf node
        if root.left == None and root.right == None:
            return 1
        #recursive calls
        if root.left:
            left_traversal =  1 + self.minDepth(root.left)
        
        if root.right:
            right_traversal = 1 + self.minDepth(root.right)
        
        return min(left_traversal,right_traversal)
        
