# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
                #base case
        if not inorder:
            return None
        
        hash_map = {}
        #print(inorder)
       
        #create hashmap
        for index,val in enumerate(inorder):
            hash_map[val] = index
        
        #create root node by popping off the first thing in preorder
        val = postorder.pop()
        #reverse the postorder list so that the root val is always last
     
        #take right and left sub_trees
        left_inorder = inorder[:hash_map[val]]
        right_inorder = inorder[hash_map[val]+1:]
        #build left and right subtrees with recursive call
        right = self.buildTree(right_inorder,postorder)
        left = self.buildTree(left_inorder,postorder)
        
        #create tree
        root = TreeNode(val = val, left = left, right = right)
        
        #return the tree
        return root
