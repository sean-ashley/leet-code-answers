# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global ret

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        ret = []
        self.traverse(root,ret)
        return ret
    
    
    def traverse(self,root,ret):
        if root:
            self.traverse(root.left,ret)
            ret.append(root.val)
            self.traverse(root.right,ret)
            
