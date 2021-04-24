# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.left_total = 0
    def sumOfLeftLeaves(self, root: TreeNode,left_node = False) -> int:
        #base case
        if not root:
            return
        #add to our total if were at a left leaf node 
        if left_node and (not root.left) and (not root.right):
           
            self.left_total += root.val
            
        #traverse the left tree and the right tree
        self.sumOfLeftLeaves(root.left,left_node = True)
        self.sumOfLeftLeaves(root.right,left_node = False)
            
        return self.left_total
