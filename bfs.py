# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        deque,ret = deque(),[]
        
        if root:
            deque.append(root)
        
        
        while deque:
            level,size = [],len(deque)
            for i in range(size):
                node = deque.popleft()
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                
                if node.right:
                    deque.append(node.right)
                    
            ret.append(level)
        
        return ret
        
