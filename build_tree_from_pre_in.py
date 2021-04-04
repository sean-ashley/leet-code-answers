# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        #base case
        if not inorder:
            return None
        
        hash_map = {}
        
        #create hashmap
        for index,val in enumerate(inorder):
            hash_map[val] = index
        
        #create root node by popping off the first thing in preorder
        val = preorder.pop(0)
        #take right and left sub_trees
        left_inorder = inorder[:hash_map[val]]
        right_inorder = inorder[hash_map[val]+1:]
        #build left and right subtrees with recursive call
        left = self.buildTree(preorder,left_inorder)
        right = self.buildTree(preorder,right_inorder)
        #create tree
        root = TreeNode(val = val, left = left, right = right)
        
        #return the tree
        return root
        
