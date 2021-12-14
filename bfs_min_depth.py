# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        #edge case
        if not root:
            return 0
        depth = 1
        queue = deque([root])
        
        while queue:
            
            level_size = len(queue)
            
            while level_size > 0:
                
                #pop out the  value in the root
                curr = queue.pop()
            
                #check if its a root node
                if curr.left == None and curr.right == None:
                    return depth

                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
                level_size -= 1
                
            depth += 1
            
            
